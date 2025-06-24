import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import logging
import os
import sys
import boto3
import pyodbc
from dataclasses import dataclass, asdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('unsigned_notes_processor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class ProcessedNote:
    """Data class for storing processed note information"""
    encounter_id: str
    patient_id: str
    document_id: str
    original_text: str
    ai_enhanced_text: str
    recommendations: str
    processed_at: datetime
    status: str = 'pending'

class DatabaseManager:
    """Manages SQL Server database operations"""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        logger.info("Initializing database connection")
        self._init_database()
    
    def _init_database(self):
        """Initialize database tables if they don't exist"""
        create_table_sql = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='processed_notes' AND xtype='U')
        CREATE TABLE processed_notes (
            id INT IDENTITY(1,1) PRIMARY KEY,
            encounter_id VARCHAR(255) NOT NULL,
            patient_id VARCHAR(255) NOT NULL,
            document_id VARCHAR(255),
            original_text NVARCHAR(MAX),
            ai_enhanced_text NVARCHAR(MAX),
            recommendations NVARCHAR(MAX),
            processed_at DATETIME NOT NULL,
            status VARCHAR(50) DEFAULT 'pending',
            created_at DATETIME DEFAULT GETDATE(),
            updated_at DATETIME DEFAULT GETDATE()
        )
        """
        
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute(create_table_sql)
                conn.commit()
                logger.info("Database tables initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            raise
    
    def save_processed_note(self, note: ProcessedNote):
        """Save a processed note to the database"""
        insert_sql = """
        INSERT INTO processed_notes 
        (encounter_id, patient_id, document_id, original_text, ai_enhanced_text, 
         recommendations, processed_at, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute(insert_sql, (
                    note.encounter_id,
                    note.patient_id,
                    note.document_id,
                    note.original_text,
                    note.ai_enhanced_text,
                    note.recommendations,
                    note.processed_at,
                    note.status
                ))
                conn.commit()
                logger.info(f"Saved processed note for encounter {note.encounter_id}")
        except Exception as e:
            logger.error(f"Error saving processed note: {e}")
            raise
    
    def get_pending_notes(self) -> List[Dict]:
        """Retrieve all pending notes from the database"""
        query = """
        SELECT * FROM processed_notes 
        WHERE status = 'pending'
        ORDER BY created_at DESC
        """
        
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Error retrieving pending notes: {e}")
            return []

class BedrockAIProcessor:
    """Handles AI processing using AWS Bedrock"""
    
    def __init__(self, aws_region: str = 'us-east-1'):
        logger.info(f"Initializing AWS Bedrock client in region {aws_region}")
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=aws_region
        )
        self.model_id = 'anthropic.claude-v2'  # or your preferred model
    
    def enhance_clinical_note(self, chart_data: Dict) -> Tuple[str, str]:
        """Process clinical note with AI and return enhanced version and recommendations"""
        
        # Extract relevant information from chart data
        patient_info = chart_data.get('data', {}).get('patient', {})
        encounter_info = chart_data.get('data', {}).get('encounter', {})
        clinical_notes = chart_data.get('data', {}).get('clinical_notes', [])
        conditions = chart_data.get('data', {}).get('conditions', [])
        medications = chart_data.get('data', {}).get('medications', [])
        vital_signs = chart_data.get('data', {}).get('vital_signs', [])
        
        # Build context for AI
        context = self._build_clinical_context(
            patient_info, encounter_info, clinical_notes, 
            conditions, medications, vital_signs
        )
        
        # Create prompt for Bedrock
        prompt = f"""You are a clinical documentation assistant helping to enhance medical notes.
        
Based on the following patient chart information, please:
1. Enhance the clinical note with proper medical terminology and completeness
2. Provide specific recommendations for documentation improvement
3. Ensure all relevant diagnoses and treatments are properly documented

Patient Context:
{context}

Please provide:
1. An enhanced version of the clinical note
2. Specific recommendations for the provider

Format your response as:
ENHANCED NOTE:
[Your enhanced note here]

RECOMMENDATIONS:
[Your recommendations here]
"""
        
        try:
            # Call Bedrock API
            body = json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 2000,
                "temperature": 0.3,
                "top_p": 0.9,
            })
            
            response = self.bedrock.invoke_model(
                body=body,
                modelId=self.model_id,
                accept='application/json',
                contentType='application/json'
            )
            
            response_body = json.loads(response.get('body').read())
            ai_response = response_body.get('completion', '')
            
            # Parse the response
            enhanced_note, recommendations = self._parse_ai_response(ai_response)
            
            logger.info("Successfully processed note with AI")
            return enhanced_note, recommendations
            
        except Exception as e:
            logger.error(f"Error processing with Bedrock: {e}")
            return "", f"Error processing note: {str(e)}"
    
    def _build_clinical_context(self, patient_info, encounter_info, clinical_notes, 
                               conditions, medications, vital_signs) -> str:
        """Build a context string from patient data"""
        context_parts = []
        
        # Patient demographics
        if patient_info:
            name = patient_info.get('name', [{}])[0].get('text', 'Unknown')
            birth_date = patient_info.get('birthDate', 'Unknown')
            gender = patient_info.get('gender', 'Unknown')
            context_parts.append(f"Patient: {name}, DOB: {birth_date}, Gender: {gender}")
        
        # Current conditions
        if conditions:
            condition_texts = []
            for condition in conditions[:5]:  # Limit to top 5
                code_text = condition.get('code', {}).get('text', '')
                if code_text:
                    condition_texts.append(code_text)
            if condition_texts:
                context_parts.append(f"Active Conditions: {', '.join(condition_texts)}")
        
        # Current medications
        if medications:
            med_texts = []
            for med in medications[:5]:  # Limit to top 5
                med_text = med.get('medicationCodeableConcept', {}).get('text', '')
                if med_text:
                    med_texts.append(med_text)
            if med_texts:
                context_parts.append(f"Current Medications: {', '.join(med_texts)}")
        
        # Recent vital signs
        if vital_signs:
            vital_summary = []
            for vital in vital_signs[:3]:  # Most recent 3
                code = vital.get('code', {}).get('text', '')
                value = vital.get('valueQuantity', {})
                if code and value:
                    vital_summary.append(f"{code}: {value.get('value')} {value.get('unit', '')}")
            if vital_summary:
                context_parts.append(f"Recent Vitals: {'; '.join(vital_summary)}")
        
        # Clinical notes preview
        if clinical_notes:
            for note in clinical_notes[:2]:  # First 2 notes
                note_type = note.get('type', {}).get('text', 'Clinical Note')
                context_parts.append(f"\n{note_type} (Preview)")
        
        return "\n".join(context_parts)
    
    def _parse_ai_response(self, response: str) -> Tuple[str, str]:
        """Parse the AI response into enhanced note and recommendations"""
        enhanced_note = ""
        recommendations = ""
        
        if "ENHANCED NOTE:" in response and "RECOMMENDATIONS:" in response:
            parts = response.split("RECOMMENDATIONS:")
            enhanced_part = parts[0].split("ENHANCED NOTE:")[1].strip()
            recommendations_part = parts[1].strip()
            
            enhanced_note = enhanced_part
            recommendations = recommendations_part
        else:
            # Fallback if format is different
            enhanced_note = response
            recommendations = "Please review the enhanced note for accuracy."
        
        return enhanced_note, recommendations

def load_config():
    """Reads the config.json file and returns the active env settings"""
    with open('config.json', 'r') as f:
        config_data = json.load(f)
        active_env = config_data['active_environment']
        logger.info(f"Running in {active_env.upper()} environment.")
        return config_data[active_env]
    
def get_access_token(config):
    """Uses client credentials to get an OAuth2 access token."""
    logger.info("Requesting access token")
    token_url = config['token_url']
    
    payload = {
        'grant_type': 'client_credentials',
        'client_id': config['client_id'],
        'client_secret': config['client_secret'],
        'scope': 'system/*.*' 
    }
    
    try:
        response = requests.post(token_url, data=payload)
        response.raise_for_status() 
        
        token_data = response.json()
        access_token = token_data['access_token']
        logger.info("Successfully obtained access token!")
        return access_token
        
    except requests.exceptions.HTTPError as err:
        logger.error(f"Error getting access token: {err}")
        if hasattr(err.response, 'text'):
            logger.error(f"Response Body: {err.response.text}")
        return None

def get_patients(config, access_token):
    """Gets a list of patients from the FHIR server."""
    logger.info("Fetching patient list")
    base_url = config['base_fhir_url']
    patients_url = f"{base_url}/Patient"
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/fhir+json'
    }
    
    try:
        response = requests.get(patients_url, headers=headers)
        response.raise_for_status()
        
        patient_bundle = response.json()
        
        patient_count = len(patient_bundle.get('entry', []))
        logger.info(f"Successfully fetched a bundle with {patient_count} patients.")
        
        if patient_count > 0:
            first_patient = patient_bundle['entry'][0]['resource']
            patient_name = first_patient['name'][0]['text']
            logger.info(f"The first patient's name is: {patient_name}")
            
    except requests.exceptions.HTTPError as err:
        logger.error(f"Error fetching patients: {err}")
        if hasattr(err.response, 'text'):
            logger.error(f"Response Body: {err.response.text}")

def make_fhir_request(url: str, access_token: str) -> Optional[Dict]:
    """Makes a FHIR API request with proper headers and error handling."""
    logger.debug(f"Making FHIR request to: {url}")
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/fhir+json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        logger.error(f"Error making FHIR request to {url}: {err}")
        if hasattr(err.response, 'text'):
            logger.error(f"Response Body: {err.response.text}")
        return None

def get_all_pages(initial_url: str, access_token: str, max_pages: int = 10) -> List[Dict]:
    """Fetches all pages of a paginated FHIR Bundle response."""
    logger.info(f"Starting paginated fetch from: {initial_url}")
    all_entries = []
    next_url = initial_url
    page_count = 0
    
    while next_url and page_count < max_pages:
        bundle = make_fhir_request(next_url, access_token)
        if not bundle:
            break
            
        entries = bundle.get('entry', [])
        all_entries.extend(entries)
        logger.debug(f"Page {page_count + 1}: Retrieved {len(entries)} entries")
        
        # Find the 'next' link for pagination
        next_url = None
        for link in bundle.get('link', []):
            if link.get('relation') == 'next':
                next_url = link.get('url')
                break
        
        page_count += 1
        if next_url:
            logger.info(f"Fetching page {page_count + 1}...")
    
    logger.info(f"Pagination complete. Total entries: {len(all_entries)}")
    return all_entries

def check_encounter_signature(encounter: Dict) -> bool:
    """Checks if an encounter has a signature extension indicating it's signed."""
    extensions = encounter.get('extension', [])
    for ext in extensions:
        # Look for the Encounter Signature Extension
        if 'encounter-signature' in ext.get('url', '').lower():
            # Check if it indicates the encounter is signed
            value = ext.get('valueBoolean') or ext.get('valueString')
            if value:
                logger.debug(f"Encounter {encounter.get('id')} is signed")
                return True
    return False

def get_encounter_documents(config: Dict, access_token: str, encounter_id: str) -> List[Dict]:
    """Gets all DocumentReferences associated with an encounter."""
    logger.info(f"Fetching documents for encounter: {encounter_id}")
    base_url = config['base_fhir_url']
    url = f"{base_url}/DocumentReference?encounter={encounter_id}"
    
    entries = get_all_pages(url, access_token)
    documents = [entry['resource'] for entry in entries if 'resource' in entry]
    logger.info(f"Found {len(documents)} documents for encounter {encounter_id}")
    return documents

def count_unsigned_documents(documents: List[Dict]) -> int:
    """Counts the number of unsigned/preliminary documents."""
    unsigned_count = 0
    
    for doc in documents:
        # Check document status - preliminary or current documents might be unsigned
        status = doc.get('status', '')
        
        # Check for docStatus if available
        doc_status = doc.get('docStatus', {})
        
        # Consider a document unsigned if:
        # 1. Status is 'preliminary' or
        # 2. No docStatus or docStatus indicates unsigned
        if status == 'preliminary' or not doc_status:
            unsigned_count += 1
            logger.debug(f"Document {doc.get('id')} is unsigned (status: {status})")
    
    return unsigned_count

def find_encounters_with_unsigned_notes(config: Dict, access_token: str, days_back: int = 30) -> List[Dict]:
    """Finds encounters with more than 1 unsigned note."""
    logger.info(f"Searching for encounters with unsigned notes from the last {days_back} days")
    base_url = config['base_fhir_url']
    
    # Calculate date for filtering recent encounters
    date_filter = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    
    # Fetch recent encounters (both in-progress and finished)
    url = f"{base_url}/Encounter?status=in-progress,finished&date=ge{date_filter}&_sort=-date&_count=50"
    
    logger.info(f"Searching for encounters from the last {days_back} days...")
    entries = get_all_pages(url, access_token, max_pages=5)
    
    qualifying_encounters = []
    total_checked = 0
    
    for entry in entries:
        encounter = entry.get('resource', {})
        encounter_id = encounter.get('id')
        total_checked += 1
        
        if not encounter_id:
            continue
        
        # Check if encounter is already signed
        if check_encounter_signature(encounter):
            continue
        
        # Get documents for this encounter
        documents = get_encounter_documents(config, access_token, encounter_id)
        
        # Count unsigned documents
        unsigned_count = count_unsigned_documents(documents)
        
        if unsigned_count > 1:
            patient_ref = encounter.get('subject', {}).get('reference', '')
            patient_id = patient_ref.split('/')[-1] if patient_ref else None
            
            qualifying_encounters.append({
                'encounter_id': encounter_id,
                'patient_id': patient_id,
                'unsigned_document_count': unsigned_count,
                'encounter_status': encounter.get('status'),
                'encounter_date': encounter.get('period', {}).get('start', 'Unknown'),
                'encounter': encounter,
                'documents': documents  # Include documents for later processing
            })
            
            logger.info(f"Found encounter {encounter_id} with {unsigned_count} unsigned documents")
    
    logger.info(f"Checked {total_checked} encounters, found {len(qualifying_encounters)} with unsigned notes")
    return qualifying_encounters

def collect_patient_chart(config: Dict, access_token: str, patient_id: str, encounter_id: str) -> Dict:
    """Collects all relevant patient chart data for AI processing."""
    logger.info(f"Collecting chart data for patient {patient_id}, encounter {encounter_id}")
    base_url = config['base_fhir_url']
    
    chart_data = {
        'patient_id': patient_id,
        'encounter_id': encounter_id,
        'collected_at': datetime.now().isoformat(),
        'data': {}
    }
    
    # 1. Patient Demographics
    logger.debug("Fetching patient demographics")
    patient_data = make_fhir_request(f"{base_url}/Patient/{patient_id}", access_token)
    if patient_data:
        chart_data['data']['patient'] = patient_data
    
    # 2. Encounter Details
    logger.debug("Fetching encounter details")
    encounter_data = make_fhir_request(f"{base_url}/Encounter/{encounter_id}", access_token)
    if encounter_data:
        chart_data['data']['encounter'] = encounter_data
    
    # 3. Clinical Notes (all for patient)
    logger.debug("Fetching clinical notes")
    doc_url = f"{base_url}/DocumentReference?patient={patient_id}&_count=100"
    doc_entries = get_all_pages(doc_url, access_token)
    chart_data['data']['clinical_notes'] = [entry['resource'] for entry in doc_entries if 'resource' in entry]
    
    # 4. Diagnoses (Conditions)
    logger.debug("Fetching diagnoses")
    condition_url = f"{base_url}/Condition?patient={patient_id}&category=encounter-diagnosis,problem-list-item&_count=100"
    condition_entries = get_all_pages(condition_url, access_token)
    chart_data['data']['conditions'] = [entry['resource'] for entry in condition_entries if 'resource' in entry]
    
    # 5. Allergies
    logger.debug("Fetching allergies")
    allergy_url = f"{base_url}/AllergyIntolerance?patient={patient_id}&_count=100"
    allergy_entries = get_all_pages(allergy_url, access_token)
    chart_data['data']['allergies'] = [entry['resource'] for entry in allergy_entries if 'resource' in entry]
    
    # 6. Medications
    logger.debug("Fetching medications")
    med_url = f"{base_url}/MedicationRequest?patient={patient_id}&_count=100"
    med_entries = get_all_pages(med_url, access_token)
    chart_data['data']['medications'] = [entry['resource'] for entry in med_entries if 'resource' in entry]
    
    # 7. Vital Signs (recent)
    logger.debug("Fetching vital signs")
    vitals_url = f"{base_url}/Observation?patient={patient_id}&category=vital-signs&_sort=-date&_count=50"
    vitals_entries = get_all_pages(vitals_url, access_token)
    chart_data['data']['vital_signs'] = [entry['resource'] for entry in vitals_entries if 'resource' in entry]
    
    # 8. Problem List
    logger.debug("Fetching problem list")
    problem_url = f"{base_url}/Condition?patient={patient_id}&category=problem-list-item&_count=100"
    problem_entries = get_all_pages(problem_url, access_token)
    chart_data['data']['problem_list'] = [entry['resource'] for entry in problem_entries if 'resource' in entry]
    
    logger.info(f"Chart collection complete for patient {patient_id}")
    return chart_data

def save_chart_data(chart_data: Dict, output_dir: str = "chart_exports"):
    """Saves the collected chart data to a JSON file."""
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create filename with patient and encounter ID
    filename = f"{output_dir}/patient_{chart_data['patient_id']}_encounter_{chart_data['encounter_id']}.json"
    
    with open(filename, 'w') as f:
        json.dump(chart_data, f, indent=2)
    
    logger.info(f"Chart data saved to: {filename}")
    return filename

def update_document_with_recommendations(config: Dict, access_token: str, 
                                       document_id: str, original_text: str, 
                                       enhanced_text: str, recommendations: str) -> bool:
    """Updates a DocumentReference with AI recommendations as a comparison"""
    logger.info(f"Updating document {document_id} with AI recommendations")
    base_url = config['base_fhir_url']
    
    try:
        # First, get the current document
        doc_url = f"{base_url}/DocumentReference/{document_id}"
        current_doc = make_fhir_request(doc_url, access_token)
        
        if not current_doc:
            logger.error(f"Could not retrieve document {document_id}")
            return False
        
        # Create a new version with AI recommendations appended
        comparison_text = f"""
{original_text}

========== AI ENHANCED VERSION (For Review) ==========
{enhanced_text}

========== AI RECOMMENDATIONS ==========
{recommendations}

========== END AI SUGGESTIONS ==========
Note: Please review the AI suggestions above and edit as needed before signing.
"""
        
        # Update the document content
        # This assumes the document has a content element with attachment
        if 'content' in current_doc and len(current_doc['content']) > 0:
            # Update the attachment data (base64 encoded)
            import base64
            encoded_content = base64.b64encode(comparison_text.encode('utf-8')).decode('utf-8')
            current_doc['content'][0]['attachment']['data'] = encoded_content
            current_doc['content'][0]['attachment']['contentType'] = 'text/plain'
            
            # Add a note about AI enhancement
            current_doc['description'] = "AI-enhanced version pending provider review"
            
            # Update the document
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/fhir+json',
                'Accept': 'application/fhir+json'
            }
            
            response = requests.put(doc_url, 
                                  headers=headers, 
                                  data=json.dumps(current_doc))
            
            if response.status_code in [200, 201]:
                logger.info(f"Successfully updated document {document_id}")
                return True
            else:
                logger.error(f"Failed to update document. Status: {response.status_code}")
                logger.error(f"Response: {response.text}")
                return False
        else:
            logger.error("Document structure does not support content update")
            return False
            
    except Exception as e:
        logger.error(f"Error updating document: {e}")
        return False

def process_unsigned_notes_batch(config: Dict, access_token: str, 
                               db_manager: Optional[DatabaseManager] = None,
                               ai_processor: Optional[BedrockAIProcessor] = None,
                               days_back: int = 30, max_encounters: int = 10):
    """Main function to process encounters with unsigned notes."""
    logger.info("\n=== Starting Unsigned Notes Batch Processing ===\n")
    
    # Find encounters with unsigned notes
    qualifying_encounters = find_encounters_with_unsigned_notes(config, access_token, days_back)
    
    if not qualifying_encounters:
        logger.info("No encounters found with more than 1 unsigned note.")
        return
    
    logger.info(f"Found {len(qualifying_encounters)} encounters with unsigned notes.")
    logger.info(f"Processing up to {max_encounters} encounters...\n")
    
    processed_charts = []
    
    # Process each encounter
    for i, encounter_info in enumerate(qualifying_encounters[:max_encounters]):
        logger.info(f"\n--- Processing {i+1}/{min(len(qualifying_encounters), max_encounters)} ---")
        logger.info(f"Encounter ID: {encounter_info['encounter_id']}")
        logger.info(f"Patient ID: {encounter_info['patient_id']}")
        logger.info(f"Unsigned Documents: {encounter_info['unsigned_document_count']}")
        logger.info(f"Encounter Date: {encounter_info['encounter_date']}")
        
        # Collect full patient chart
        chart_data = collect_patient_chart(
            config, 
            access_token, 
            encounter_info['patient_id'], 
            encounter_info['encounter_id']
        )
        
        # Save the chart data
        filename = save_chart_data(chart_data)
        
        # Process with AI if processor available
        if ai_processor:
            logger.info("Processing with AI...")
            enhanced_text, recommendations = ai_processor.enhance_clinical_note(chart_data)
            
            # Process each unsigned document
            for doc in encounter_info.get('documents', []):
                if doc.get('status') == 'preliminary' or not doc.get('docStatus'):
                    doc_id = doc.get('id')
                    original_text = "Original clinical note text"  # Extract from document
                    
                    # Save to database if available
                    if db_manager:
                        processed_note = ProcessedNote(
                            encounter_id=encounter_info['encounter_id'],
                            patient_id=encounter_info['patient_id'],
                            document_id=doc_id,
                            original_text=original_text,
                            ai_enhanced_text=enhanced_text,
                            recommendations=recommendations,
                            processed_at=datetime.now()
                        )
                        db_manager.save_processed_note(processed_note)
                    
                    # Update the document with recommendations
                    success = update_document_with_recommendations(
                        config, access_token, doc_id, 
                        original_text, enhanced_text, recommendations
                    )
                    
                    if success:
                        logger.info(f"Updated document {doc_id} with AI recommendations")
        
        processed_charts.append({
            'filename': filename,
            'encounter_id': encounter_info['encounter_id'],
            'patient_id': encounter_info['patient_id'],
            'unsigned_count': encounter_info['unsigned_document_count']
        })
    
    # Summary
    logger.info("\n=== Processing Complete ===")
    logger.info(f"Total encounters processed: {len(processed_charts)}")
    logger.info("\nExported files:")
    for chart in processed_charts:
        logger.info(f"  - {chart['filename']}")
    
    logger.info("\nThese files have been processed and recommendations added to the EHR.")
    
    return processed_charts

# --- Main execution ---
if __name__ == "__main__":
    # Load configuration
    app_config = load_config()
    
    # Initialize database if SQL Server connection string is provided
    db_manager = None
    if os.environ.get('SQL_CONNECTION_STRING'):
        db_manager = DatabaseManager(os.environ['SQL_CONNECTION_STRING'])
    
    # Initialize AI processor if AWS credentials are configured
    ai_processor = None
    if os.environ.get('AWS_ACCESS_KEY_ID'):
        ai_processor = BedrockAIProcessor()
    
    # Get access token
    token = get_access_token(app_config)
    
    if token:
        # Process unsigned notes
        process_unsigned_notes_batch(
            config=app_config,
            access_token=token,
            db_manager=db_manager,
            ai_processor=ai_processor,
            days_back=30,  # Look back 30 days
            max_encounters=5  # Process up to 5 encounters as a test
        )
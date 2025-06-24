# Azalea Health Unsigned Notes Processor

This application connects to the Azalea Health FHIR API to identify patient encounters with multiple unsigned clinical notes, collects comprehensive chart data, processes it with AWS Bedrock AI, and updates the EHR with recommendations for provider review.

## Purpose

Help healthcare providers at Comprehensive Medical Clinic clear their backlog of unsigned notes by:
1. Finding encounters with >1 unsigned clinical notes
2. Collecting all relevant patient chart data
3. Processing with AWS Bedrock AI for note enhancement
4. Updating notes in EHR with AI recommendations for comparison
5. Storing results in SQL Server for tracking

## Features

- **Automated Discovery**: Finds encounters with multiple unsigned notes
- **Comprehensive Data Collection**: Gathers complete patient chart information
- **AI Enhancement**: Uses AWS Bedrock to enhance clinical documentation
- **EHR Integration**: Updates notes with AI suggestions for provider review
- **SQL Server Storage**: Tracks all processed notes and recommendations
- **Comprehensive Logging**: Full audit trail of all operations
- **Sandbox Support**: Test safely in sandbox environment before production

## Setup

### Prerequisites
- Python 3.7+
- Access to Azalea Health API (client credentials)
- AWS Account with Bedrock access
- SQL Server database (optional)

### Installation
```bash
# Clone the repository
git clone [your-repo-url]
cd azalea_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

#### 1. API Configuration
The `config.json` file contains your API credentials:
- `client_id`: Your application's client ID
- `client_secret`: Your application's client secret
- `token_url`: OAuth token endpoint
- `base_fhir_url`: FHIR API base URL
- `active_environment`: Switch between "sandbox" and "production"

**Important**: Keep your `client_secret` secure and never commit it to version control.

#### 2. Environment Variables
Create a `.env` file with the following variables:

```bash
# SQL Server Connection (optional)
SQL_CONNECTION_STRING=Driver={ODBC Driver 17 for SQL Server};Server=your-server.database.windows.net;Database=your-database;Uid=your-username;Pwd=your-password;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;

# AWS Credentials for Bedrock
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_DEFAULT_REGION=us-east-1

# Optional: Override Bedrock model
BEDROCK_MODEL_ID=anthropic.claude-v2
```

## Usage

### Basic Usage
```python
python main.py
```

This will:
1. Authenticate with the API (using sandbox by default)
2. Search for encounters from the last 30 days
3. Find encounters with >1 unsigned notes
4. Collect full patient chart data
5. Process with AWS Bedrock AI (if configured)
6. Update documents in EHR with AI recommendations
7. Save results to SQL Server (if configured)
8. Create JSON exports in `chart_exports/` directory
9. Log all operations to `unsigned_notes_processor.log`

### Customization
You can modify the parameters in the main function call:

```python
process_unsigned_notes_batch(
    config=app_config,
    access_token=token,
    db_manager=db_manager,      # SQL Server connection (optional)
    ai_processor=ai_processor,  # AWS Bedrock processor (optional)
    days_back=30,              # Look back N days for encounters
    max_encounters=5           # Process up to N encounters
)
```

## Architecture

### Components

1. **FHIR API Client**: Handles all API interactions with Azalea Health
2. **DatabaseManager**: Manages SQL Server operations for tracking processed notes
3. **BedrockAIProcessor**: Interfaces with AWS Bedrock for AI processing
4. **Document Updater**: Updates EHR documents with AI recommendations

### Data Flow

1. **Discovery**: Find encounters with unsigned notes
2. **Collection**: Gather comprehensive patient data
3. **Processing**: Send to AWS Bedrock for enhancement
4. **Storage**: Save to SQL Server for tracking
5. **Update**: Push recommendations back to EHR
6. **Review**: Provider reviews and approves/edits suggestions

## Output

### JSON Files
Created in `chart_exports/` directory:
```
patient_[PATIENT_ID]_encounter_[ENCOUNTER_ID].json
```

### SQL Server Records
Stored in `processed_notes` table with:
- Original and enhanced text
- AI recommendations
- Processing timestamps
- Status tracking

### EHR Updates
Documents are updated with a comparison format:
```
[Original Note]

========== AI ENHANCED VERSION (For Review) ==========
[AI Enhanced Note]

========== AI RECOMMENDATIONS ==========
[Specific Recommendations]

========== END AI SUGGESTIONS ==========
Note: Please review the AI suggestions above and edit as needed before signing.
```

## Data Structure

```json
{
  "patient_id": "12345",
  "encounter_id": "67890",
  "collected_at": "2024-01-01T10:00:00",
  "data": {
    "patient": { /* FHIR Patient resource */ },
    "encounter": { /* FHIR Encounter resource */ },
    "clinical_notes": [ /* Array of DocumentReference resources */ ],
    "conditions": [ /* Array of Condition resources */ ],
    "allergies": [ /* Array of AllergyIntolerance resources */ ],
    "medications": [ /* Array of MedicationRequest resources */ ],
    "vital_signs": [ /* Array of Observation resources */ ],
    "problem_list": [ /* Array of Condition resources */ ]
  }
}
```

## Logging

The application provides comprehensive logging:
- **Console Output**: Real-time progress updates
- **Log File**: `unsigned_notes_processor.log` with detailed operations
- **Log Levels**: INFO for normal operations, ERROR for issues, DEBUG for troubleshooting

## Security Considerations

- Always use HTTPS connections
- Store credentials securely (use environment variables)
- Limit API scope to minimum required permissions
- Ensure HIPAA compliance when handling PHI
- Implement audit logging for production use
- Use sandbox for testing before production
- Encrypt data at rest in SQL Server
- Follow AWS best practices for Bedrock access

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify client_id and client_secret
   - Check if application has required scopes
   - Ensure using correct environment (sandbox vs production)

2. **No Encounters Found**
   - Adjust `days_back` parameter to search wider date range
   - Verify organization has encounters with unsigned notes
   - Check encounter status filters
   - Review logs for specific errors

3. **AWS Bedrock Errors**
   - Verify AWS credentials are set correctly
   - Check Bedrock service availability in your region
   - Ensure your AWS account has Bedrock access enabled
   - Review model ID configuration

4. **SQL Server Connection Issues**
   - Verify connection string format
   - Check firewall rules
   - Ensure ODBC driver is installed
   - Test connection with SQL Server Management Studio

5. **API Rate Limits**
   - Implement delays between requests if needed
   - Process in smaller batches
   - Contact Azalea Health for rate limit information

## Production Deployment

1. **Switch to Production**:
   - Update `active_environment` in config.json to "production"
   - Update base_fhir_url to your organization's endpoint

2. **Security Hardening**:
   - Use Azure Key Vault or AWS Secrets Manager for credentials
   - Implement proper access controls
   - Enable audit logging

3. **Monitoring**:
   - Set up alerts for processing failures
   - Monitor API usage and rate limits
   - Track AI processing costs

4. **Backup & Recovery**:
   - Regular SQL Server backups
   - Archive processed JSON files
   - Document recovery procedures

## Next Steps

After implementation:
1. Monitor provider adoption and feedback
2. Fine-tune AI prompts based on results
3. Implement automated scheduling for batch processing
4. Build dashboard for tracking progress
5. Add support for different note types
6. Integrate with provider workflow tools

## Support

- **API Issues**: Contact Azalea Health support
- **AWS Bedrock**: Check AWS documentation and support
- **Application Issues**: Review logs and `unsigned_notes_plan.md`

## License

[Your License Here] 
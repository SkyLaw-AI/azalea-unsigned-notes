# Azalea Health API - Unsigned Notes Processing Plan

## Overview
Create an application to fetch patient charts for encounters with >1 unsigned notes from Comprehensive Medical Clinic's Azalea Health EHR, process them with AWS Bedrock AI, and update the EHR with recommendations for provider review.

## Current Setup
- **Organization**: Comprehensive Medical Clinic LLC (ID: 142219)
- **API**: Azalea Health FHIR R4 API
- **Auth**: OAuth 2.0 Client Credentials
- **Base URL (Sandbox)**: https://app.azaleahealth.com/fhir/R4/sandbox
- **Base URL (Production)**: https://app.azaleahealth.com/fhir/R4/142219
- **Environment**: Currently set to SANDBOX for safe testing

## Implementation Plan

### Phase 1: Authentication ✅
- ✅ OAuth 2.0 client credentials implementation
- ✅ Environment switching (sandbox/production)
- ✅ Token management with system/*.* scope
- ✅ Comprehensive error handling

### Phase 2: Find Encounters with Unsigned Notes ✅
1. ✅ Fetch recent encounters (status=in-progress or finished)
2. ✅ Check for Encounter Signature Extension
3. ✅ Get DocumentReferences for each encounter
4. ✅ Filter encounters with >1 unsigned/preliminary documents
5. ✅ Pagination support for large datasets
6. ✅ Detailed logging of discovery process

### Phase 3: Collect Patient Chart Data ✅
For each qualifying encounter, collect:
- ✅ Patient demographics
- ✅ Encounter details
- ✅ Clinical notes (all types)
- ✅ Diagnoses (Conditions)
- ✅ Allergies
- ✅ Medications
- ✅ Vital signs
- ✅ Problem list

### Phase 4: AI Processing & Storage ✅
1. ✅ AWS Bedrock integration for AI processing
2. ✅ Clinical context building for accurate AI recommendations
3. ✅ SQL Server database for tracking processed notes
4. ✅ Structured prompt engineering for medical documentation
5. ✅ Error handling and fallback mechanisms

### Phase 5: EHR Updates ✅
1. ✅ Update DocumentReference with AI recommendations
2. ✅ Comparison format for provider review
3. ✅ Preserve original content with AI suggestions
4. ✅ Clear labeling of AI-generated content

## Technical Architecture

### Components Implemented:
1. **DatabaseManager Class**
   - SQL Server connection management
   - Table initialization
   - CRUD operations for processed notes
   - Error handling and logging

2. **BedrockAIProcessor Class**
   - AWS Bedrock client initialization
   - Clinical context extraction
   - Prompt engineering for medical notes
   - Response parsing and formatting

3. **Document Update System**
   - FHIR DocumentReference updates
   - Base64 encoding for content
   - Comparison format generation
   - PUT operation implementation

4. **Comprehensive Logging**
   - File and console output
   - Multiple log levels (INFO, ERROR, DEBUG)
   - Detailed operation tracking
   - Audit trail for compliance

## API Endpoints Used

### Core Resources
- `/Encounter` - Find encounters
- `/DocumentReference` - Get clinical notes and update them
- `/Patient` - Demographics
- `/Condition` - Diagnoses & problems
- `/AllergyIntolerance` - Allergies
- `/MedicationRequest` - Medications
- `/Observation` - Vital signs

### Key Filters
- Encounters: `?status=in-progress,finished&date=ge[date]&_sort=-date`
- Documents: `?encounter=[id]&category=clinical-note`
- Conditions: `?patient=[id]&category=encounter-diagnosis,problem-list-item`
- Observations: `?patient=[id]&category=vital-signs`

## Environment Variables Required
```bash
# SQL Server (optional)
SQL_CONNECTION_STRING=<your-connection-string>

# AWS Bedrock
AWS_ACCESS_KEY_ID=<your-key>
AWS_SECRET_ACCESS_KEY=<your-secret>
AWS_DEFAULT_REGION=us-east-1

# Optional
BEDROCK_MODEL_ID=anthropic.claude-v2
```

## Database Schema
```sql
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
```

## Output Format in EHR
Documents are updated with:
```
[Original Note Content]

========== AI ENHANCED VERSION (For Review) ==========
[AI Enhanced Version]

========== AI RECOMMENDATIONS ==========
[Specific Recommendations]

========== END AI SUGGESTIONS ==========
Note: Please review the AI suggestions above and edit as needed before signing.
```

## Security Considerations Implemented
1. ✅ Environment-based configuration
2. ✅ Secure credential storage via environment variables
3. ✅ HTTPS-only communication
4. ✅ Comprehensive error handling without exposing sensitive data
5. ✅ Audit logging for all operations
6. ✅ Sandbox testing before production

## Current Status
- ✅ Core functionality complete
- ✅ AWS Bedrock integration implemented
- ✅ SQL Server tracking implemented
- ✅ Document update capability added
- ✅ Comprehensive logging throughout
- ✅ Sandbox testing environment configured
- ✅ Production-ready architecture

## Usage Summary
1. Set environment to sandbox in config.json
2. Configure environment variables (.env file)
3. Run `python main.py`
4. Monitor logs for progress
5. Review updated documents in EHR
6. Check SQL Server for tracking data
7. Switch to production when ready

## Future Enhancements
1. ⏳ Automated scheduling (cron/Windows Task Scheduler)
2. ⏳ Web dashboard for monitoring progress
3. ⏳ Bulk approval interface for providers
4. ⏳ Analytics on AI recommendation acceptance rates
5. ⏳ Support for different note types (SOAP, H&P, etc.)
6. ⏳ Multi-organization support
7. ⏳ Real-time processing via webhooks 
SkyLaw - Dashboard



Partner Account Details

Name

SkyLaw

Description

Personal Injury focused medical-legal software.

Website

https://www.skylaw.ai

Phone Contact

+12166449441

Terms Agreed





Yes

Agreed On

Mon, Jun 23, 2025 at 8:34 PM EDT

Azalea Health's Terms of Use

Created

Mon, Jun 23, 2025 at 8:34 PM EDT





Developer Home





API Overview





Getting Started

Launching Applications

How to Exchange Data

Authorization & Access

U.S. Core Mappings





Compliance & Certification









Implementation Guides









Ambulatory









Hospital









Azalea One









Account





About Azalea Health





Community Help Center





Sign Out

© 2025 Azalea Health, Inc.

Developer Portal

Getting Started

Registration





Use of the Developer Portal and all Azalea Health APIs by partner applications is subject to the Terms of Use.

Step 1. Create a free Azalea Health account

Welcome to the Azalea Health API platform! We are glad that you are interested in building an integration with Azalea Health's products and services.

Before you can get started experimenting you must first register your application through the Azalea Health Developer Portal. There is no charge for registering applications, connecting to our sandbox accounts, or launching your application on our platform.

A free Azalea Health user account, along with a Partner Account, are required to get started. Once you have your Azalea Health account then simply login to continue.







 Register 



 Sign In

Step 2. Create a Partner Account

If your organization already has a partner account then please contact your administrator for access (this is likely the person who set up the account with us). Otherwise, log into the developer portal and then click "Create Account".

Fill out the fields as follows:

Company Name: The name of your company.

Description: A short description about your company.

Website: The company's website.

Phone Contact: A primary phone contact for the company.

Terms of Use: Agree to Azalea Health's terms of use.

Step 3. Create an Application

Go to the Applications section of your partner account portal and then click "Create Application".

Once your client application is created, it will automatically be granted access to the sandbox environment by issuing it an OAuth 2.0 client ID and secret. The application's OAuth 2.0 credentials will be available in the application's details page.

Fill out the fields as follows:

Name: The name of your application.

Description: A short description of what your application does.

Email Contact: An email contact. This defaults to the email of the account used to register the application but can always be changed.

Login URL: The login url for your application. Optional.

Redirect URLs: Required for authorization workflows.

SMART® App Type: Provider or Patient facing application.

SMART® Launch URL: Required for EHR Launch workflows.

Client authentication: Public or confidential client.

SMART® Backend Services Authorization: Enables system level authentication (client_credentials grant) and required for FHIR® Bulk Data Access (Flat FHIR®).

Authorization

Authorization is obtained by using one of the defined OAuth 2.0 authorization grants:

Grant Type

Allowed

Description

Authorization Code

Yes

The Authorization Code grant type is used by confidential and public clients to exchange an authorization code for an access token to obtain access on behalf of an authenticated user.

Client Credentials

Yes

The Client Credentials grant type is used by clients to obtain an access token outside of the context of a user, such as on behalf of some system.

Implicit

No

The Implicit grant type is a simplified flow that can be used by public clients, where the access token is returned immediately without an extra authorization code exchange step.

Password

No

The Password grant type is used by first-party clients to exchange a user's credentials for an access token.

Refresh Token

Yes

The Refresh Token grant type is used by clients to exchange a refresh token for an access token when the access token has expired.

Requesting Authorization

Please refer to the Launching Applications documentation to learn more about authorization. After successfully retrieving an access token, your application is ready to start making requests.

Accessing Resources

To access FHIR® resources utilizing an access token, include a "bearer" authorization header in your HTTP request per RFC 6750 as follows:

Authorization: Bearer eyJraWQiOiIyMDE2LTExLTAxVDE1OjExOjQ4LjY1NS5lYyIsInR5

If the access token is invalid, the FHIR® resource will return a 401 Unauthorized response:

{

"error": "access_denied",

"message": "The resource owner or authorization server denied the request."

}

All request and responses for FHIR® resources utilize the application/json, application/fhir+json, or application/json+fhir format for data exchange. Note that no other data formats are supported at this time.

Example request to read patients:

GET [base]/Patient HTTP/1.1Authorization: Bearer ...Accept: application/fhir+json

Example response:

HTTP/1.1 200 OKHost: azaleahealth.comDate: Fri, 14 Oct 2022 15:26:40 GMTConnection: closeCache-Control: no-cache, privateContent-Type: application/fhir+json{

"resourceType": "Bundle",

"type": "searchset",

"timestamp": "2022-10-12T15:55:48+00:00",

"link": [

{

"relation": "self",

"url": "[base]/Patient"

},

{

"relation": "first",

"url": "[base]/Patient?_page=1"

},

{

"relation": "next",

"url": "[base]/Patient?_page=2"

}

],

"entry": [

{

"link": [

{

"relation": "self",

"url": "[base]/Patient/cfd0d813-91d4-413c-83d5-510f25e560d3"

}

],

"resource": {

"resourceType": "Patient",

"id": "cfd0d813-91d4-413c-83d5-510f25e560d3",

"meta": {

"versionId": "1",

"lastUpdated": "2022-10-12T15:45:46-04:00",

"profile": [

"[base]/StructureDefinition/Patient",

"http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"

]

},

"text": {

"status": "generated",

"div": "Dustin Ritchie"

},

"extension": [

{

"extension": [

{

"url": "ombCategory",

"valueCoding": {

"system": "urn:oid:2.16.840.1.113883.6.238",

"code": "2186-5",

"display": "Non Hispanic or Latino"

}

},

{

"url": "text",

"valueString": "Non Hispanic or Latino"

}

],

"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"

},

{

"extension": [

{

"url": "ombCategory",

"valueCoding": {

"system": "urn:oid:2.16.840.1.113883.6.238",

"code": "2106-3",

"display": "White"

}

},

{

"url": "text",

"valueString": "White"

}

],

"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"

},

{

"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",

"valueCode": "M"

}

],

"identifier": [

{

"type": {

"coding": [

{

"system": "http://terminology.hl7.org/CodeSystem/v2-0203",

"code": "MR"

}

]

},

"system": "urn:azalea:hspid",

"value": "INF.102"

},

{

"type": {

"coding": [

{

"system": "http://terminology.hl7.org/CodeSystem/v2-0203",

"code": "SS"

}

]

},

"system": "http://hl7.org/fhir/sid/us-ssn",

"value": "999619797"

},

{

"system": "urn:uuid:824bb08f-67eb-41fc-8008-290c5cec0304",

"value": "DRITCHIE"

},

{

"system": "http://hospital.smarthealthit.org",

"value": "e91975f5-9445-c11f-cabf-c3c6dae161f2"

}

],

"active": true,

"name": [

{

"use": "maiden",

"text": "Dusty Ritchie",

"family": "Ritchie",

"given": [

"Dusty"

],

"period": {

"start": "1940-09-05T04:00:00.000-04:00",

"end": "1960-09-05T04:00:00.000-04:00"

}

},

{

"use": "usual",

"text": "Dustin Ritchie",

"family": "Ritchie",

"given": [

"Dustin"

],

"period": {

"start": "1960-09-05T04:00:00.000-04:00",

"end": ""

}

}

],

"telecom": [

{

"system": "phone",

"value": "(555) 770-2787",

"use": "home"

}

],

"gender": "male",

"birthDate": "1940-09-05",

"deceasedBoolean": false,

"address": [

{

"use": "home",

"text": "599 Schowalter Promenade, West Springfield, MA 01089",

"line": [

"599 Schowalter Promenade"

],

"city": "West Springfield",

"state": "MA",

"postalCode": "01089",

"country": "US",

"period": {

"start": "1940-09-05T04:00:00.000-04:00"

}

}

],

"maritalStatus": {

"coding": [

{

"system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",

"code": "M",

"display": "Married",

"userSelected": true

}

]

},

"multipleBirthBoolean": false,

"communication": [

{

"language": {

"coding": [

{

"system": "urn:iso:std:iso:6392",

"code": "eng",

"display": "English",

"userSelected": true

}

]

},

"preferred": true

}

]

},

"search": {

"mode": "match"

}

}

]

}

Capabilities

Dynamic discovery of the FHIR® resource server's capabilities - which portions of the HL7® FHIR® specification it supports - is performed by an HTTP GET command to the /metadata endpoint as shown:

GET [base]/CapabilityStatement/metadata HTTP/1.1

The resource server returns a CapabilityStatement resource. Using the Accept: text/html header returns the Capability Statement in an easy to read HTML format.

Requirements for Production Access

You can request production access via the portal on the application screen. Our API team will review the application to determine whether production credentials can be granted.

Marketplace

Creating a listing on the Azalea Apps marketplace promotes visibility and usage of your application. From the Partner Account view, you can access the Partner Portal to manage your listing. Managing your company profile allows you to edit client-facing information about your organization. Managing company apps allows you to edit information about the services you offer. You can also upload additional materials to accompany your listing.

References

The OAuth 2.0 Authorization Framework

OAuth 2.0 Threat Model and Security Considerations

OAuth 2.0 Security Best Current Practice

OAuth 2.0 for Native Apps

HTTP Authentication: Basic and Digest Access Authentication

The OAuth 2.0 Authorization Framework: Bearer Token Usage

HL7® FHIR® Specification

SMART® App Launch Framework

SMART® Scopes and Launch Context

HL7 FHIR® US Core Implementation Guide STU3 Release 3.1.1





Need technical assistance? Please contact us through our Community Help Center. Use of the Azalea Developer portal is subject to the Terms of Use.



Launching Applications

SMART App Launch Framework

Azalea Health supports the SMART App Launch Framework v1.0.0 for connecting third-party applications to Electronic Health Record data. Our product platforms support the following use cases:

Patient apps that launch standalone

Provider apps that launch standalone

Provider apps that launch from within the EHR

Bulk Data Access (Flat FHIR®)

Registering a SMART App

Before a SMART app can be launched the app must be registered with the Azalea Health Developer Portal.

When registering an application that needs to run in a provider (or clinical) context, choose the Provider SMART App Type.

When registering an application that needs to run in a patient (or PHR) context, choose the Patient SMART App Type.

Launch Implementation Guides

Please refer to the following guides for each SMART App Launch workflow:

Standalone Launch v1.0.0

EHR Launch v1.0.0

Bulk Data Access







Developer Home





API Overview





Getting Started

Launching Applications

How to Exchange Data

Authorization & Access

U.S. Core Mappings





Compliance & Certification









Implementation Guides









Ambulatory









Hospital









Azalea One









Account





About Azalea Health





Community Help Center





Sign Out

© 2025 Azalea Health, Inc.

Developer Portal

How to Exchange Data

Introduction

Azalea Health follows the HL7® FHIR® resource model for enabling data exchange between applications and Azalea Health's product platforms. FHIR® is 'RESTful' framework centered around 'resources' and a set of operations known as 'interactions' on resources. Individual resources are managed in collections organized around their type - such as 'Patient' or 'Encounter'.

If you are new to FHIR® then we suggest that you read their summary to get started.

Interactions

Resources support several standard interactions for reading and writing data (note that not all resources will support writing data back into the system).

Instance Level InteractionsreadRead the current state of the resourceupdateUpdate an existing resource by its id (or create it if it is new)patchUpdate an existing resource by posting a set of changes to itdeleteDelete a resourceType Level InteractionscreateCreate a new resource with a server assigned idsearchSearch the resource type based on some filter criteriaWhole System InteractionscapabilitiesGet a capability statement for the systembatch/transactionUpdate, create or delete a set of resources in a single interaction

Additional information about the RESTful HTTP model can be found on the FHIR® website.

Service Base URL

The Service Base URL is the address where all of the resources defined by this interface are found. Please refer to the specific product platform documentation to find the service base URL. The Service Base URL takes the form of:

http{s}://server{/path}

All the logical interactions are defined relative to the service root URL. This means that if the address of any one FHIR® resource on a system is known, the address of other resources may be determined.

Search Parameters

Search operations traverse through an existing set of resources filtering by parameters supplied to the search operation.

The following search result parameters are supported across all resource types:

Parameter Name

Type

Description

_count

number

The maximum number of results to return. If not provided, then the default max will be returned.

Example: ?_count=20

_elements

string

A comma-separated list of base element names to be returned. Only elements that are listed will be returned along with any mandatory and modifier elements.

_sort

string

A comma-separated list of sort rules in priority order.

Example: ?_sort=status,-date,category

_summary

string

Returns a subset of the resource. Values can be: true, text, data, count, or false.

_total

string

Provides the total number of matching resources in Bundle.total.

Example: ?_total=accurate

In addition, there is a special search parameter _filter that allows for an alternative method of searching, and the parameter _format defined for all interactions.

In the simplest case, a search is executed by performing a GET operation in the RESTful framework:

GET [base]/[type]?name=value&...{&_format=[mime-type]}}

For this RESTful search, the parameters are a series of name=[value] pairs encoded in the URL or as an application/x-www-form-urlencoded submission for a POST:

POST [base]/[type]/_search{?[parameters]{&_format=[mime-type]}}

The server determines which of the set of resources it serves meet the specific criteria, and returns the results in the HTTP response as a bundle which includes the resources that are the results of the search.

Paging

When a search request has more results than can be returned in a single request the result set will be paged. The client must use the server supplied links in Bundle.link in order to traverse the pages.

This example shows the third page of a search result:

{

"resourceType": "Bundle",

"link": [

{

"relation": "self",

"url": "http://example.org/Patient?name=peter&stateid=23&_page=3"

},

{

"relation": "first",

"url": "http://example.org/Patient?name=peter&stateid=23&_page=1"

},

{

"relation": "previous",

"url": "http://example.org/Patient?name=peter&stateid=23&_page=2"

},

{

"relation": "next",

"url": "http://example.org/Patient?name=peter&stateid=23&_page=4"

},

{

"relation": "last",

"url": "http://example.org/Patient?name=peter&stateid=23&_page=26"

}

]

}

Note that a link to the last page will not be available unless the client requests the total number of resources returned via the _total=accurate parameter.

In the case of a search, the initial request may be made via a POST, but the follow up page links will be formatted as GET requests. Clients may opt to convert follow up page links to a POST request.

Updating Resources

There are two approaches to updating resources where the update operation is supported: PUT and PATCH.

PUT

With a PUT operation you MUST include the entire representation of the resource (as returned by a GET request) along with any modified values. Do NOT submit a summarized payload as an update! In other words, the PUT operation replaces the server representation with the one you are sending. There are some exceptions to this, such as elements that cannot be changed via an update operation. For example, the meta.lastUpdated and meta.profile elements and identifiers assigned by the EHR. Some resources may not support changing the values of certain elements as part of an update request in order to maintain system integrity. For example, some clinical resources may not allow the patient subject to be changed once the resource is created. See the resource documentation if you are unsure.

PATCH

With a PATCH operation, however, you can modify individual elements without referencing the full representation. All PATCH operations require a payload with valid JSON Patch syntax as described here: https://jsonpatch.com/. The Content-Type header in your PATCH request must be set to application/json-patch+json.

For example, to update just the status element on an Appointment resource to cancelled:

PATCH [base]/Appointment/[id]

Content-Type: application/json-patch+json

[

{"op": "replace", "path": "status", "value": "cancelled"}

]

Errors

When things go wrong, the API will respond with an error HTTP status code and a human-readable description to describe the incorrect submission.

Status Code

Meaning

400

Bad input. There is an error with the input that usually can be corrected by the client (write).

401

Unauthorized. Missing or expired Authorization token.

403

Forbidden. The client or user does not have the required scope or permission to perform the action.

404

Resource instance not found (read, update, and delete).

405

Method not allowed. The operation is not supported by the resource.

422

Validation error. One or more validation errors were triggered by the input (write).

500

Internal server error. There is a problem with the server and the request cannot be completed at this time.



Output

Name

Type

Description

Is Optional

OperationOutcome

OperationOutcome

See the OperationOutcome.issue element for error details.

No

OperationOutcome.issue.severity

code

fatal | error | warning | information

No

OperationOutcome.issue.details

CodeableConcept

Additional details about the error

No

Token Revocation

Users can revoke application access through the Azalea Health Account Management Portal by navigating to "Connected Apps" and selecting "Revoke". Any active access tokens and related refresh tokens are then revoked for the application.

Authorization & Access

Introduction

Access control generally consists of multiple interconnected components:

Identification - Who are you? Usually a user name or email and a User ID.

Authentication - Prove your identity. Usually a password or other secret.

Authorization - What are you allowed to read or change? Usually a scope or permission.

Identification

When an app is accessing resources on behalf of a user the user will be identified by their unique Azalea Health Single Sign On user account ID which is formatted as a UUID.

Azalea Health's FHIR APIs follow the SMART App Launch v1.0.0 specification for requesting identity data. This can be accomplished by requesting a pair of OpenID Connect scopes: openid and fhirUser. When these scopes are requested (and the request is granted), the app will receive an id_token that comes alongside the access token. The id_token value is a JWT or JSON Web Token. To learn more about the user, the app should treat the fhirUser claim as the URL of a FHIR resource representing the current user. This will be a resource of type Person.

Steps for using an ID token

Examine the ID token for its “issuer” property

Perform a GET {issuer}/.well-known/openid-configuration

Fetch the server's JSON Web Key by following the “jwks_uri” property

Validate the token's signature against the public key from step #3

Extract the fhirUser claim from the id_token JWT and treat it as the URL of a FHIR Person resource

Authentication

Azalea Health's FHIR API authentication is build on SMART on FHIR which is in turn built on OAuth2. Apps registered with Azalea Health are issued an OAuth2 client_id and client_secret (one per app). These are in turn used to authenticate your app with the FHIR server when requesting an access token. Apps that can keep their client_secret confidential (either through storage or transmission) may exchange their client_id and client_secret pair for an access token. Apps that cannot keep their client_secret confidential (i.e., the app is running in a web browser) shoud use the Proof Key for Code Exchange (PKCE) extension to OAuth2, which is fully supported by Azalea Health's authentication service.

An app that is revoked (either by the developer or by Azalea Health) will be denied all forms of authentication.

Authorization

Authorization by default is based on SMART on FHIR and more specifically the Scopes and Launch Context defined by it. The SMART specification is released in two different version as of the date of publication: SMART v1 and SMART v2. Only Smart v1 is currently supported at this time. SMART defines a syntax for rules, using so called “scope”-claims, to specify the precise access rights that a user wants to delegate to an external application on their behalf.

These are examples of scopes that are recognized (SMART v1):

scope=user/Observation.read: the user is allowed to read Observation resources

scope=user/Encounter.write: the user is allowed to write Encounter resources

scope=user/*.read: the user is allowed to read any type of resource

scope=user/*.write: the user is allowed to write any type of resource

scope=[array of individual scopes]

When a client app wants to access data in a FHIR Server on behalf of its user, it requests a token from the authorization server. The configuration of the authorization server determines which claims are available for a the app. The client app configuration determines which claims it needs. During the token request, the user is usually redirected to the authorization server, logs in and is then asked whether the client app is allowed to receive the requested claims. The client app cannot request any claims that are not available to that application. For details on how to retrieve an access token as an application, please refer to SMART App Launch.



When an app requests a resource that its authorization token is not scoped to the FHIR server will respond with a HTTP 401 (Unauthorized).

Bulk Data Access

When an app is using the Bulk Data Access model for authentication then it must pre-register a list of "allowed" system context scopes that it needs to perform its requirements. This list should as narrow as possible and avoid using broad wild-card scopes. ONLY scopes registered in the app's allowed list will be permitted at authorization time.

These are examples of scopes that are recognized (Bulk Data v1):

scope=system/Observation.read: the app is allowed to read Observation resources

scope=system/Encounter.write: the app is allowed to write Encounter resources

scope=system/*.read: the app is allowed to read any type of resource

scope=system/*.write: the app is allowed to write any type of resource

scope=[array of individual scopes]

Additional User Restrictions

Apps that are accessing resources may be subject to additional user level restrictions imposed by the EHR platform such as permissions (access control system) or other visibility restrictions specific to that user account. Either or both may result in HTTP 403 (Forbidden) responses or data being inaccessible via search or read requests that result in HTTP 404 (Not Found).

It is the responsibility of the app developer to properly handle user specific restrictions.

U.S. Core Mappings

Details

Azalea Health is committed to providing applications with access to a wide variety of health information including, but not limited to, U.S. Core Data for Interoperability – or USCDI - data classes and elements. The following page explains how to map USCDI data back to Azalea Health's FHIR® resources.

USCDI Version

V1

U.S. Core Version

3.1.1

Data ElementUS Core ProfileFHIR® ResourceAllergies and Intolerances:Substance (Medication)US Core Allergies ProfileAllergyIntoleranceSubstance (Drug Class)US Core Allergies ProfileAllergyIntoleranceReactionUS Core Allergies ProfileAllergyIntoleranceAssessment and Plan of TreatmentUS Core CarePlan ProfileCarePlanCare Team MembersUS Core CareTeam ProfileCareTeamClinical Notes:Consultation NoteUS Core DocumentReference ProfileDocumentReferenceDischargeUS Core DocumentReference ProfileDocumentReferenceSummary NoteUS Core DocumentReference ProfileDocumentReferenceHistory & PhysicalUS Core DocumentReference ProfileDocumentReferenceImaging NarrativeUS Core DocumentReference Profile , US Core DiagnosticReport Profile for Report and Note exchangeDocumentReference, DiagnosticReportLaboratory Report NarrativeUS Core DocumentReference Profile , US Core DiagnosticReport Profile for Report and Note exchangeDocumentReference, DiagnosticReportPathology Report NarrativeUS Core DocumentReference Profile , US Core DiagnosticReport Profile for Report and Note exchangeDocumentReference, DiagnosticReportProcedure NoteUS Core DocumentReference Profile , US Core DiagnosticReport Profile for Report and Note exchangeDocumentReference, DiagnosticReportProgress NoteUS Core DocumentReference ProfileDocumentReferenceConsultation NoteUS Core DocumentReference ProfileDocumentReferenceGoals:Patient GoalsUS Core Goal ProfileGoalHealth ConcernsUS Core Condition ProfileConditionImmunizationsUS Core Immunization ProfileImmunizationLaboratory:TestsUS Core Laboratory Result Observation Profile , US Core DiagnosticReport Profile for Laboratory Results ReportingObservation, DiagnosticReportValues/ResultsUS Core Laboratory Result Observation Profile , US Core DiagnosticReport Profile for Laboratory Results ReportingObservation, DiagnosticReportMedications:MedicationsUS Core Medication Profile , US Core Medication Request ProfileMedication, MedicationRequestMedication AllergiesUS Core Allergies ProfileAllergyIntolerancePatient Demographics:First NameUS Core Patient ProfilePatient.name.givenLast NameUS Core Patient ProfilePatient.name.familyPrevious NameUS Core Patient ProfilePatient.nameMiddle Name (including middle initial)US Core Patient ProfilePatient.name.givenSuffixUS Core Patient ProfilePatient.name.suffixBirth SexUS Core Patient ProfileUS Core Birth Sex ExtensionDate of BirthUS Core Patient ProfilePatient.birthDateRaceUS Core Patient ProfileUS Core Race ExtensionEthnicityUS Core Patient ProfileUS Core Ethnicity ExtensionPreferred LanguageUS Core Patient ProfilePatient.communicationAddressUS Core Patient ProfilePatient.addressPhone NumberUS Core Patient ProfilePatient.telecomProblemsUS Core Condition ProfileConditionProceduresUS Core Procedure ProfileProcedureProvenance:US Core Provenance ProfileProvenanceAuthor Time StampUS Core Provenance ProfileProvenance.recordedAuthor OrganizationUS Core Provenance ProfileProvenance.agentSmoking StatusUS Core Smoking Status Observation ProfileObservationUnique Device Identifier(s) for a Patient's Implantable Device(s)US Core Implantable Device ProfileDeviceVital Signs:Diastolic blood pressureBlood pressure systolic and diastolic (FHIR® Core Profile)ObservationSystolic blood pressureBlood pressure systolic and diastolic (FHIR® Core Profile)ObservationBody heightBody height (FHIR® Core Profile)ObservationBody weightBody weight (FHIR® Core Profile)ObservationHeart rateHeart rate (FHIR® Core Profile)ObservationRespiratory rateRespiratory rate (FHIR® Core Profile)ObservationBody temperatureBody temperature (FHIR® Core Profile)ObservationPulse oximetryUS Core Pulse Oximetry Profile (Builds on FHIR® Core Profile)ObservationInhaled oxygen concentrationUS Core Pulse Oximetry Profile (Builds on FHIR® Core Profile)ObservationBMI Percentile (2-20 years old)US Core Pediatric BMI for Age Observation Profile (Builds on FHIR® Core Profile)ObservationWeight-for-length Percentile (Birth - 36 months)US Core Pediatric Weight for Height Observation Profile (Builds on FHIR® Core Profile)ObservationOccipital-frontal Head Circumference Percentile (Birth - 36 months)US Core Pediatric Head Occipital Frontal Circumference Observation Profile (Builds on FHIR® Core Profile)Observation



---

SMART on FHIR App Launch

Overview

The SMART App Launch Implementation Guide facilitates the integration of third-party applications with Electronic Health Record data, enabling their launch from within or outside the EHR system's user interface. It offers a robust and secure authorization protocol for various app architectures, accommodating both end-user device-based apps and those operating on a secure server, accessible to clinicians, patients, and others through PHRs, Patient Portals, or any FHIR based system.



SMART App Launch Type

Version

Supported

Documentation

Standalone Launch

v1.0.0

Yes

Official specification

Azalea implementation guide

Standalone Launch

v2.0.0

No

EHR Launch

v1.0.0

Yes

Official specification

Azalea implementation guide

EHR Launch

v2.0.0

No

--







Developer Home





API Overview









Compliance & Certification









Implementation Guides





SMART App Launch

Standalone Launch v1.0.0

EHR Launch v1.0.0

Bulk Data Access

Bulk Data Export

Clinical Notes





Ambulatory









Hospital









Azalea One









Account





About Azalea Health





Community Help Center





Sign Out

© 2025 Azalea Health, Inc.

Developer Portal

SMART v1.0.0 Standalone Launch

Standalone Launch Sequence

When an application launches standalone it is launched from outside of an existing EHR session. The user will be required to login using their Azalea Health credentials and grant access to the application. The user will also be prompted to either accept all of the applications requested scopes or selectively enable certain scopes.

In order to obtain launch context and request authorization to access FHIR® resources, the app discovers the Azalea EHR authorization server's OAuth authorize and token endpoint URLs by querying their [base].well-known/smart-configuration.json file. The app then can declare its launch context requirements by adding specific scopes to the request it sends to Azalea EHR's authorization server. The authorize endpoint will acquire the context the app needs and make it available.

If the app needs patient context then it can provide the launch scope launch/patient and the user will be prompted to select a patient prior to the app launching.



Workflow

Step 1: App asks for authorization

Step 2: EHR evaluates authorization request, asking for end-user input

Step 3: App exchanges authorization code for access token

Step 4: App accesses clinical data via FHIR® API

Step 5: (Later…) App uses a refresh token to obtain a new access token

SMART Authorization

Step 1: App asks for authorization



At launch time, the app constructs a request for authorization by adding the following parameters to the query component of Azalea EHR's "authorize” endpoint URL.:

Parameters

response_type

Required

Must be code

client_id

Required

The client's identifier.

redirect_uri

Required

Must match one of the client's pre-registered redirect URIs.

scope

Required

Must describe the access that the app needs, including clinical data scopes like patient/*.read, openid and fhirUser (if app needs authenticated patient identity) and:

a set of launch context requirements in the form launch/patient, which asks Azalea EHR to establish context on your behalf.

See SMART on FHIR® Access Scopes details.

state

Required

An opaque value used by the client to maintain state between the request and callback. The authorization server includes this value when redirecting the user-agent back to the client. The parameter SHALL be used for preventing cross-site request forgery or session fixation attacks.

aud

Required

URL of the Azalea EHR resource server from which the app wishes to retrieve FHIR® data (see the platform specific documentation for FHIR® server base URLs). This parameter prevents leaking a genuine bearer token to a counterfeit resource server.



Requesting Identity

If the app needs to authenticate the identity of the end-user, it should include two OpenID Connect scopes: openid and fhirUser. When these scopes are requested, and the request is granted, the app will receive an id_token along with the access token. For full details, see SMART launch context parameters.

For example:

If an app needs demographics and observations for a single patient, and also wants information about the current logged-in user, the app can request:

patient/Patient.read

patient/Observation.read

openid fhirUser

Scopes

Access to protected resources are negotiated via OAuth 2.0 scopes and a launch context. During the authorization process, client applications must identify:

The specific FHIR® resources that will be needed to accomplish the workflow.

The type of access needed to each FHIR® resource (read, write).

With SMART® on FHIR®, access to FHIR® resources is controlled by scopes with the following format:

launch-context "/" resource-type "." modification-rights.

The "launch-context" portion represents one of three possible choices:

user

Access to the resource is only constrained by the access of the user.

patient

Access to the resource is constrained within context of a single patient.

system

Used in system-based (Bulk Data Access) authorization workflows (client_credentials grant).

Examples of scopes include:

user/Observation.read

Read all values from the Observation resource that the user has access to.

patient/MedicationStatement.read

Read medications for a specific patient.

user/Appointment.write

Create appointments

system/Patient.read

Read all values from the Patient resource for the health system.





The list of scopes supported by Azalea Health is available by making a GET request to[base]/.well-known/smart-configuration

and examining the "scopes_supported" property. System launch context requires that all scopes be pre-authorized prior to accessing resources. Requests for scopes outside of the client application's allowed scopes will be denied.

Wildcard Scopes

Client applications can request resource scopes that contain a wildcard (*) for both the FHIR® resource as well as the requested permission for the given resource. When a wildcard is requested for the FHIR® resource, the client is asking for all data for all available FHIR® resources, both now and in the future.

Examples of wildcard scopes include:

system/Patient.*

Read and write all patient data

system/*.read

Read from all available data for all resources

system/*.*

Read and write to all available data for all resources

Step 2: EHR evaluates authorization request, asking for end-user input

The authorization decision is up to the Azalea EHR authorization server, which may request authorization from the end-user. The Azalea EHR authorization server will enforce access rules based on local policies and optionally direct end-user input.

The EHR end-user decides whether to grant or deny access. This decision is communicated to the app when the Azalea EHR authorization server returns an authorization code (or, if denying access, an error response). Authorization codes are short-lived, usually expiring within around one minute. The code is sent when the Azalea EHR authorization server causes the browser to navigate to the app's redirect_uri, with the following URL parameters:

Parameters

code

Required

The authorization code generated by the authorization server. The authorization code expires shortly after it is issued in order to mitigate the risk of leaks.

state

Required

The exact value received from the client.



For example:

Location: https://app/after-auth?code=123abc&state=98wrghuwuogerg97

Step 3: App exchanges authorization code for access token

After obtaining an authorization code, the app trades the code for an access token via HTTP POST to the Azalea EHR authorization server's token endpoint URL, using content-type application/x-www-form-urlencoded.

Parameters

grant_type

Required

Fixed value: authorization_code

code

Required

Code that the app received from the authorization server

redirect_uri

Required

The same redirect_uri used in the initial authorization request

client_id

Conditional

Required for public apps. Omit for confidential apps.



The Azalea EHR authorization server will return a JSON object that includes an access token or a message indicating that the authorization request has been denied.

Launch context arrives with your access_token

Once an app is authorized, the token response will include any context data the app requested – along with (potentially!) any unsolicited context data the EHR decides to communicate.

The JSON structure includes the following parameters:

Parameters

access_token

Required

The access token issued by the authorization server

token_type

Required

Fixed value: Bearer

expires_in

Required

Lifetime in seconds of the access token, after which the token will no longer be accepted by the resource server

scope

Required

Scope of access authorized. Note that this can be different from the scopes requested by the app.

id_token

Optional

Authenticated patient identity and user details, if requested

refresh_token

Optional

Token that can be used to obtain a new access token, using the same or a subset of the original authorization grants

patient

Optional

If the app was launched from within a patient context. For example, a parameter like "patient": "123" would indicate the FHIR® resource https://[base]/Patient/123.



For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

POST /token HTTP/1.1Host: ehrAuthorization: Basic bXktYXBwOm15LWFwcC1zZWNyZXQtMTIzContent-Type: application/x-www-form-urlencodedgrant_type=authorization_code&code=123abc&redirect_uri=https%3A%2F%2Fapp%2Fafter-auth

{

"access_token": "i8hweunweunweofiwweoijewiwe",

"token_type": "bearer",

"expires_in": 3600,

"scope": "patient/Observation.read patient/Patient.read",

"patient": "123"

}

Step 4: App accesses clinical data via FHIR® API

With a valid access token, the app can access protected EHR data by issuing a FHIR® API call to the FHIR® endpoint on the EHR's resource server. The request includes an Authorization header that presents the access_token as a "Bearer" token:

Authorization: Bearer [access_token]

For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

GET [base]/Patient/123

Authorization: Bearer i8hweunweunweofiwweoijewiwe

{

"resourceType": "Patient",

"birthDate": ...

}

Step 5: (Later…) App uses a refresh token to obtain a new access token

Refresh tokens are issued to enable sessions to last longer than the validity period of an access token. The app requests a refresh token in its original authorization request via the online_access or offline_access scope (see SMART on FHIR® Access Scopes for details).

An HTTP POST transaction is made to the Azalea EHR authorization server's token URL, with content-type application/x-www-form-urlencoded

Parameters

grant_type

Required

Fixed value: refresh_token.

refresh_token

Required

The refresh token from a prior authorization response

scope

Optional

The scopes of access requested. If present, this value must be a strict sub-set of the scopes granted in the original launch (no new permissions can be obtained at refresh time). A missing value indicates a request for the same scopes granted in the original launch.



The response is a JSON object containing a new access token, with the following claims:

Parameters

access_token

Required

New access token issued by the authorization server.

token_type

Required

Fixed value: Bearer

expires_in

Required

Lifetime in seconds of the access token, after which the token will no longer be accepted by the resource server

scope

Required

Scope of access authorized. Note that this can be different from the scopes requested by the app.

refresh_token

Optional

The refresh token issued by the authorization server. If present, the app should discard any previous refresh_token associated with this launch, replacing it with this new value.



For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

POST /token HTTP/1.1Host: ehrAuthorization: Basic bXktYXBwOm15LWFwcC1zZWNyZXQtMTIzContent-Type: application/x-www-form-urlencodedgrant_type=refresh_token&refresh_token=a47txjiipgxkvohibvsm

{

"access_token": "m7rt6i7s9nuxkjvi8vsx",

"token_type": "bearer",

"expires_in": 3600,

"scope": "patient/Observation.read patient/Patient.read",

"refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA"

}

--







Developer Home





API Overview









Compliance & Certification









Implementation Guides





SMART App Launch

Standalone Launch v1.0.0

EHR Launch v1.0.0

Bulk Data Access

Bulk Data Export

Clinical Notes





Ambulatory









Hospital









Azalea One









Account





About Azalea Health





Community Help Center





Sign Out

© 2025 Azalea Health, Inc.

Developer Portal

SMART v1.0.0 EHR Launch

EHR launch sequence

In SMART's EHR launch flow, a user has established an existing Azalea EHR session, and then decides to launch an app. This could be a single-patient app (which runs in the context of a patient record), or a user-level app (like an appointment manager or a population dashboard). Azalea EHR initiates a "launch sequence" by opening a new browser instance (or iframe) pointing to the app's registered launch URL and passing some context.

The following parameters are included:

Parameters

iss

Required

Identifies the EHR's FHIR® endpoint, which the app can use to obtain additional details about the EHR, including its authorization URL.

launch

Required

Opaque identifier for this specific launch, and any EHR context associated with it. This parameter must be communicated back to the EHR at authorization time by passing along a launch parameter (see example below).

A launch might cause the browser to navigate to:

Location: https://app/launch?iss=https://ehr/fhir&launch=xyz123

On receiving the launch notification, the app would query the issuer's /metadata/ endpoint or .well-known/smart-configuration.json endpoint which contains (among other details) the OAuth authorize and token endpoint URLs for use in requesting authorization to access FHIR® resources.

Later, when the app prepares a list of access scopes to request from the Azalea EHR authorization server, it will be associated with the existing Azalea EHR context by including the launch notification in the scope.



SMART Actions

An app can only be launched from within the EHR by defining one or more SMART Actions. At this time, SMART Actions can only be configured by Azalea Health. Please contact us if you wish to make use of EHR Launch.

Each SMART Action consists of the following properties:

Name - This will be the name of the link inside the EHR

SMART Launch URL - A URL controlled by the target app that handles the the start of the launch sequence.

Intent - An arbirary string defined by the app to help distinguish between multiple actions.

Placement - An EHR specific set of codes that control where the link appears in the EHR and what context may be provided.

Workflow

Step 1: App asks for authorization

Step 2: EHR evaluates authorization request, asking for end-user input

Step 3: App exchanges authorization code for access token

Step 4: App accesses clinical data via FHIR® API

Step 5: (Later…) App uses a refresh token to obtain a new access token

SMART Authorization

Step 1: App asks for authorization



At launch time, the app constructs a request for authorization by adding the following parameters to the query component of Azalea EHR's "authorize” endpoint URL.:

Parameters

response_type

Required

Must be code

client_id

Required

The client's identifier.

redirect_uri

Required

Must match one of the client's pre-registered redirect URIs.

launch

Required

When using the EHR launchflow, this must match the launch value received from the EHR.

scope

Required

Must describe the access that the app needs, including clinical data scopes like patient/*.read, openid and fhirUser (if app needs authenticated patient identity) and:

a set of launch context requirements in the form launch/patient, which asks Azalea EHR to establish context on your behalf.

See SMART on FHIR® Access Scopes details.

state

Required

An opaque value used by the client to maintain state between the request and callback. The authorization server includes this value when redirecting the user-agent back to the client. The parameter SHALL be used for preventing cross-site request forgery or session fixation attacks.

aud

Required

URL of the Azalea EHR resource server from which the app wishes to retrieve FHIR® data (see the platform specific documentation for FHIR® server base URLs). This parameter prevents leaking a genuine bearer token to a counterfeit resource server. In the case of an EHR launch flow, this aud value is the same as the launch's iss value.



Requesting Identity

If the app needs to authenticate the identity of the end-user, it should include two OpenID Connect scopes: openid and fhirUser. When these scopes are requested, and the request is granted, the app will receive an id_token along with the access token. For full details, see SMART launch context parameters.

For example:

If an app needs demographics and observations for a single patient, and also wants information about the current logged-in user, the app can request:

patient/Patient.read

patient/Observation.read

openid fhirUser

Scopes

Access to protected resources are negotiated via OAuth 2.0 scopes and a launch context. During the authorization process, client applications must identify:

The specific FHIR® resources that will be needed to accomplish the workflow.

The type of access needed to each FHIR® resource (read, write).

With SMART® on FHIR®, access to FHIR® resources is controlled by scopes with the following format:

launch-context "/" resource-type "." modification-rights.

The "launch-context" portion represents one of three possible choices:

user

Access to the resource is only constrained by the access of the user.

patient

Access to the resource is constrained within context of a single patient.

system

Used in system-based (Bulk Data Access) authorization workflows (client_credentials grant).

Examples of scopes include:

user/Observation.read

Read all values from the Observation resource that the user has access to.

patient/MedicationStatement.read

Read medications for a specific patient.

user/Appointment.write

Create appointments

system/Patient.read

Read all values from the Patient resource for the health system.





The list of scopes supported by Azalea Health is available by making a GET request to[base]/.well-known/smart-configuration

and examining the "scopes_supported" property. System launch context requires that all scopes be pre-authorized prior to accessing resources. Requests for scopes outside of the client application's allowed scopes will be denied.

Wildcard Scopes

Client applications can request resource scopes that contain a wildcard (*) for both the FHIR® resource as well as the requested permission for the given resource. When a wildcard is requested for the FHIR® resource, the client is asking for all data for all available FHIR® resources, both now and in the future.

Examples of wildcard scopes include:

system/Patient.*

Read and write all patient data

system/*.read

Read from all available data for all resources

system/*.*

Read and write to all available data for all resources

Step 2: EHR evaluates authorization request, asking for end-user input

The authorization decision is up to the Azalea EHR authorization server, which may request authorization from the end-user. The Azalea EHR authorization server will enforce access rules based on local policies and optionally direct end-user input.

The EHR end-user decides whether to grant or deny access. This decision is communicated to the app when the Azalea EHR authorization server returns an authorization code (or, if denying access, an error response). Authorization codes are short-lived, usually expiring within around one minute. The code is sent when the Azalea EHR authorization server causes the browser to navigate to the app's redirect_uri, with the following URL parameters:

Parameters

code

Required

The authorization code generated by the authorization server. The authorization code expires shortly after it is issued in order to mitigate the risk of leaks.

state

Required

The exact value received from the client.



For example:

Location: https://app/after-auth?code=123abc&state=98wrghuwuogerg97

Step 3: App exchanges authorization code for access token

After obtaining an authorization code, the app trades the code for an access token via HTTP POST to the Azalea EHR authorization server's token endpoint URL, using content-type application/x-www-form-urlencoded.

Parameters

grant_type

Required

Fixed value: authorization_code

code

Required

Code that the app received from the authorization server

redirect_uri

Required

The same redirect_uri used in the initial authorization request

client_id

Conditional

Required for public apps. Omit for confidential apps.



The Azalea EHR authorization server will return a JSON object that includes an access token or a message indicating that the authorization request has been denied.

Launch context arrives with your access_token

Once an app is authorized, the token response will include any context data the app requested – along with (potentially!) any unsolicited context data the EHR decides to communicate. If your SMART Action configured an intent value then this will be returned here (see below).

The JSON structure includes the following parameters:

Parameters

access_token

Required

The access token issued by the authorization server

token_type

Required

Fixed value: Bearer

expires_in

Required

Lifetime in seconds of the access token, after which the token will no longer be accepted by the resource server

scope

Required

Scope of access authorized. Note that this can be different from the scopes requested by the app.

id_token

Optional

Authenticated patient identity and user details, if requested

refresh_token

Optional

Token that can be used to obtain a new access token, using the same or a subset of the original authorization grants

smart_style_url

Optional

String URL where the host’s style parameters can be retrieved (for apps that support styling)

intent

Optional

String value describing the intent of the application launch (for SMART Actions that configure intent)

patient

Optional

If the app was launched from within a patient context. For example, a parameter like "patient": "123" would indicate the FHIR® resource https://[base]/Patient/123.



For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

POST /token HTTP/1.1Host: ehrAuthorization: Basic bXktYXBwOm15LWFwcC1zZWNyZXQtMTIzContent-Type: application/x-www-form-urlencodedgrant_type=authorization_code&code=123abc&redirect_uri=https%3A%2F%2Fapp%2Fafter-auth

{

"access_token": "i8hweunweunweofiwweoijewiwe",

"token_type": "bearer",

"expires_in": 3600,

"scope": "patient/Observation.read patient/Patient.read",

"smart_style_url": "https://ehr/styles/smart_v1.json",

"intent": "make-payment",

"patient": "123"

}

Step 4: App accesses clinical data via FHIR® API

With a valid access token, the app can access protected EHR data by issuing a FHIR® API call to the FHIR® endpoint on the EHR's resource server. The request includes an Authorization header that presents the access_token as a "Bearer" token:

Authorization: Bearer [access_token]

For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

GET [base]/Patient/123

Authorization: Bearer i8hweunweunweofiwweoijewiwe

{

"resourceType": "Patient",

"birthDate": ...

}

Step 5: (Later…) App uses a refresh token to obtain a new access token

Refresh tokens are issued to enable sessions to last longer than the validity period of an access token. The app requests a refresh token in its original authorization request via the online_access or offline_access scope (see SMART on FHIR® Access Scopes for details).

An HTTP POST transaction is made to the Azalea EHR authorization server's token URL, with content-type application/x-www-form-urlencoded

Parameters

grant_type

Required

Fixed value: refresh_token.

refresh_token

Required

The refresh token from a prior authorization response

scope

Optional

The scopes of access requested. If present, this value must be a strict sub-set of the scopes granted in the original launch (no new permissions can be obtained at refresh time). A missing value indicates a request for the same scopes granted in the original launch.



The response is a JSON object containing a new access token, with the following claims:

Parameters

access_token

Required

New access token issued by the authorization server.

token_type

Required

Fixed value: Bearer

expires_in

Required

Lifetime in seconds of the access token, after which the token will no longer be accepted by the resource server

scope

Required

Scope of access authorized. Note that this can be different from the scopes requested by the app.

refresh_token

Optional

The refresh token issued by the authorization server. If present, the app should discard any previous refresh_token associated with this launch, replacing it with this new value.



For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

POST /token HTTP/1.1Host: ehrAuthorization: Basic bXktYXBwOm15LWFwcC1zZWNyZXQtMTIzContent-Type: application/x-www-form-urlencodedgrant_type=refresh_token&refresh_token=a47txjiipgxkvohibvsm

{

"access_token": "m7rt6i7s9nuxkjvi8vsx",

"token_type": "bearer",

"expires_in": 3600,

"scope": "patient/Observation.read patient/Patient.read",

"refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA"

}

--

Bulk Data Access

Overview

The FHIR Bulk Data Access Implementation Guide is designed to facilitate the seamless exchange of large-scale healthcare data.

Existing FHIR APIs work well for accessing small amounts of data, but large exports can require hundreds of thousands of requests. This implementation guide defines a standardized, FHIR based approach for exporting bulk data from a FHIR server to a pre-authorized client.

Additionally, Bulk Data Access provides a framework for connecting third-party applications to Electronic Health Record data in a background or system context without user authorization.

In this scenario, applications MUST have their required scopes pre-authorized through the Developer Portal prior to authorizing their application. After registration, you will need to add your desired scopes in the Edit Application Details page. Finally, apps MUST be pre-authorized with each specific tenant account before they can pull that tenant's data. Pre-authorization requires approval from Azalea Health and the specific tenant account.



Implementation

Version

Supported

Documentation

Bulk Data Export

v1.0.0

Yes

Bulk Data Access STU1

Backend Services Authorization

Azalea implementation guide

Requesting Authorization on Behalf of a System

The following illustrates how to authorize on behalf of a backend system using the OAuth 2.0 client_credentials grant type.

This involves the following steps:

Discover the token endpoint URL.

Construct and invoke a token request.

Receive the OAuth 2.0 bearer token.

Handle any exceptions encountered.

Start making FHIR® API requests.

Discovering the Token URL

Azalea Health's FHIR® servers advertise the URL of its respective authorization server within its FHIR® conformance document.

The FHIR® Conformance resource can be retrieved by performing an HTTP GET against the /.well-known/smart-configuration endpoint, which is relative to the FHIR® base URL. Within the structure of this document you will find the token endpoint identified by the "token_endpoint" property.

GET [base]/.well-known/smart-configuration HTTP/1.1

{

"authorization_endpoint": "[base]/oauth/authorize",

"token_endpoint": "[base]/oauth/token",

"scopes_supported": [],

"capabilities": []

}

Getting an Authorization Token (Confidential Clients)

Confidential applications, or applications that can securely store the client_secret value, may use the following authorization flow for obtaining an access token:

Before a SMART client can run against a FHIR® server, the client SHALL register the application and provide the following configurations in the application details page of the Azalea Health Developer Portal:

For the "Client authentication" field select Confidential client.

The SMART® Backend Services Authorization field must be checked.

An authorization request takes the form of an x-www-form-urlencoded query string, appended to the token endpoint's URL (as discovered from the previous section).

The following parameters are included in the client credentials token request:

Parameters

grant_type

Required

Must be client_credentials

client_id

Required

Your client application's identifier.

client_secret

Required

Your client application's secret key.

scope

Required

Must describe the access that the app needs, including clinical data scopes like system/Patient.read.



The authorization server will respond, upon a successful request, with the following values:

Parameters

token_type

Fixed value: Bearer.

expires_in

The number of seconds from now when the access token expires.

access_token

The access token, to be used in the Authorization header of all subsequent requests to the resource server.



Example Request:

POST [base]/oauth/token HTTP/1.1Accept: application/jsonContent-Type: application/x-www-form-urlencodedgrant_type=client_credentials

&client_id=144

&client_secret=cqwUwbiBzBKRqKo1l2

&scope=system%2FPatient.read

Example Response:

HTTP/1.1 200 OKContent-Type: application/json;charset=UTF-8Cache-Control: no-storePragma: no-cache{

"access_token": "m7rt6i7s9nuxkjvi8vsx",

"token_type": "Bearer",

"expires_in": 31622400,

"scope": "system/Patient.read"

}

At this point your application is ready to start making requests.

Getting an Authorization Token (Public Clients)

Public applications, or applications that can NOT securely store the client_secret value, may use the client assertion authorization flow for obtaining an access token:

Before a SMART client can run against a FHIR server, the client SHALL register the application and provide the following configurations in the application details page of the Azalea Health Developer Portal:

For the "Client authentication" field select Public client.

The SMART® Backend Services Authorization field must be checked.

Generate or obtain an asymmetric key pair and register your public key as either a publicly accessible JWK Set Url or paste the JWK Set JSON directly into the JWK Set Payload field.



Before a client can request an access token, it must generate a one-time-use JSON Web Token (JWT) that will be used to authenticate the client to the FHIR® authorization server. The authentication JWT SHALL include the following claims and must be signed with the client's private key (which MUST be an RS384 signature).

Authentication JWT Header Values

alg

Required

Must be RS384

kid

Required

The identifier of the key-pair used to sign this JWT. This identifier SHALL be unique within the client's JWK Set.

typ

Required

Fixed value: JWT.



Authentication JWT Claims

iss

Required

Issuer of the JWT -- the client's client_id, as determined during registration

sub

Required

The service's client_id, as determined during registration

aud

Required

The FHIR® authorization server's "token URL" (the same URL to which this authentication JWT will be posted)

exp

Required

Expiration time integer for this authentication JWT, expressed in seconds since the "Epoch" (1970-01-01T00:00:00Z UTC). This time SHALL be no more than five minutes in the future.

jti

Required

A nonce string value that uniquely identifies this authentication JWT.



After generating an authentication JWT, the client requests a new access token via HTTP POST to the Azalea Health authorization server's token endpoint URL, using content-typex-www-form-urlencoded (as discovered from the previous section).

The following parameters are included in the client credentials token request:

Parameters

grant_type

Required

Must be client_credentials

client_id

Required

Your client application's identifier.

client_assertion_type

Required

Fixed value: urn:ietf:params:oauth:client-assertion-type:jwt-bearer

client_assertion

Required

Signed authentication JWT value (see above)



Example Request:

POST [base]/oauth/token HTTP/1.1Accept: application/jsonContent-Type: application/x-www-form-urlencodedgrant_type=client_credentials

&scope=system%2F*.read%20system%2FCommunicationRequest.write

&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer

&client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzM4NCIsImtpZCI6ImVlZTlmMTdhM2I1OThmZDg2NDE3YTk4MGI1OTFmYmU2In0.eyJpc3MiOiJiaWxpX21vbml0b3IiLCJzdWIiOiJiaWxpX21vbml0b3IiLCJhdWQiOiJodHRwczovL2F1dGhvcml6ZS5zbWFydGhlYWx0aGl0Lm9yZy90b2tlbiIsImV4cCI6MTQyMjU2ODg2MCwianRpIjoicmFuZG9tLW5vbi1yZXVzYWJsZS1qd3QtaWQtMTIzIn0.l2E3-ThahEzJ_gaAK8sosc9uk1uhsISmJfwQOtooEcgUiqkdMFdAUE7sr8uJN0fTmTP9TUxssFEAQnCOF8QjkMXngEruIL190YVlwukGgv1wazsi_ptI9euWAf2AjOXaPFm6t629vzdznzVu08EWglG70l41697AXnFK8GUWSBf_8WHrcmFwLD_EpO_BWMoEIGDOOLGjYzOB_eN6abpUo4GCB9gX2-U8IGXAU8UG-axLb35qY7Mczwq9oxM9Z0_IcC8R8TJJQFQXzazo9YZmqts6qQ4pRlsfKpy9IzyLzyR9KZyKLZalBytwkr2lW7QU3tC-xPrf43jQFVKr07f9dA

Example Response:

HTTP/1.1 200 OKContent-Type: application/json;charset=UTF-8Cache-Control: no-storePragma: no-cache{

"access_token": "m7rt6i7s9nuxkjvi8vsx",

"token_type": "bearer",

"expires_in": 300,

"scope": "system/*.read system/CommunicationRequest.write"

}

For an in-depth example of issuing client assertion token requests please see the FHIR Bulk Data documentation.

Accessing clinical data via FHIR® API

With a valid access token, the app can access protected EHR data by issuing a FHIR® API call to the FHIR® endpoint on the EHR's resource server. The request includes an Authorization header that presents the access_token as a "Bearer" token:

Authorization: Bearer [access_token]

For example:

Given an authorization code, the app trades it for an access token via HTTP POST.

GET [base]/Patient/123

Authorization: Bearer i8hweunweunweofiwweoijewiwe

{

"resourceType": "Patient",

"birthDate": ...

}

Scopes

As the client authorization addressed by this specification involves no user or launch context, clients SHALL use “system” scopes that parallel SMART “user” scopes. System scopes have the format system/(:resourceType|*).(read|write|*) – which conveys the same access scope as the matching user format user/(:resourceType|*).(read|write|*).

However, system scopes MUST be pre-authorized by the application prior to obtaining access tokens.





See theSMART® Backend Authentication Scopes

section of your application's details page in the Developer Portal. You may change these scopes as often as you like until the application is approved for production access, after which you will not be able to change the authorized system scopes without contacting us.

Bulk Export

The Bulk Data Export framework can be used by applications to perform an asynchronous export of FHIR® resources. The application must obtain access via one of the two methods described above at which point it may kick off a bulk data export request. Note that only resources for which it has pre-authorized scopes can be exported.

--

Bulk Data Export

Overview

The Bulk Data Export framework can be used by applications to perform an asynchronous export of FHIR® resources. The app must obtain access via one of the two methods described in the Bulk Data Access implementation guide at which point the app may kick off a bulk data export request. Note that only resources for which the app has pre-authorized scopes can be exported.

Bulk Data Kick-off Request



All Patients export:

GET [base]/Patient/$export

Accept: application/fhir+jsonPrefer: respond-async



Single Patient export:

A single patient can be exported by adding a _typeFilter query parameter to the all patient export request to filter the Patient resource by a single _id:

GET [base]/Patient/$export?_typeFilter=Patient?_id=1234

Accept: application/fhir+jsonPrefer: respond-async



Group of Patients export:

GET [base]/Group/[id]/$export

Accept: application/fhir+jsonPrefer: respond-async

Query Parameters:

Note that all query parameters are optional.

Parameter

Type

Description

_outputFormat

string

Currently, only application/fhir+ndjson is supported.

_since

instant

Resources will be included in the response if their state has changed after the supplied time (e.g. if Resource.meta.lastUpdated is later than the supplied _since time).

_type

string

Only resources of the specified resource types(s) SHALL be included in the response. For example _type=Practitioner could be used to bulk data extract all Practitioner resources from a FHIR endpoint.

_typeFilter

string

The value of the _typeFilter parameter is a comma-separated list of FHIR REST API queries that further restrict the results of the query. For example, suppose that a client would like to restrict MedicationRequests to requests that are active, or else completed after July 1, 2018. This can be accomplished with two subqueries joined together with a comma for a logical “or”:MedicationRequest?status=active

MedicationRequest?status=completed&date=gt2018-07-01T00:00:00Z

To create a _typeFilter parameter, a client should URL encode these two subqueries and join them with comma (,):



$export?_typeFilter=MedicationRequest%3Fstatus%3Dactive,MedicationRequest%3Fstatus%3Dcompleted%26date%3Dgt2018-07-01T00%3A00%3A00Z

Response:

HTTP Status Code of 202 Accepted

Content-Location header with the absolute URL of an endpoint for subsequent status requests (polling location)

Bulk Data Delete Request

After a bulk data request has been started, a client MAY send a DELETE request to the URL provided in the Content-Location header to cancel the request.

Bulk Data Status Request

After a bulk data request has been started, the client MAY poll the status URL provided in the Content-Location header from the initial kick off request. When requesting status, the client should use an Accept header indicating a content type of application/json. Note that the content polling location requires an access token.

Example in progress response:

Status: 202 AcceptedRetry-After: 120

Example completed response:

Status: 200 OKContent-Type: application/json{

"transactionTime": "[instant]",

"request" : "[base]/Patient/$export",

"requiresAccessToken" : false,

"output" : [{

"type" : "Patient",

"url" : "https://ehr/fhir/patient_file_1.ndjson"

},{

"type" : "Patient",

"url" : "https://ehr/fhir/patient_file_2.ndjson"

},{

"type" : "Observation",

"url" : "https://ehr/fhir/observation_file_1.ndjson"

}],

"error" : [{

"type" : "OperationOutcome",

"url" : "https://ehr/fhir/outcomeoperation_error_file1.ndjson"

}],

}

--

Clinical Notes

Overview

The US Core DocumentReference Profile and US Core DiagnosticReport Profile for Report and Note Exchange support the exchange of Clinical Notes.

Common Clinical Notes

Azalea Health APIs support all five of the "Common Clinical Notes":

Consultation Note (11488-4)

Discharge Summary (18842-5)

History & Physical Note (34117-2)

Procedures Note (28570-0)

Progress Note (11506-3)

Each of the five common clinical notes are mapped to a DocumentReference where the DocumentReference.type code is a fixed LOINC as defined by the US Core 3.1.1 Clinical Note Type Value Set.

Diagnostic Notes

Azalea Health APIs support all three DiagnosticReport categories:

Cardiology (LP29708-2)

Pathology (LP7839-6)

Radiology (LP29684-5)

Each of the five common clinical notes are mapped to a DiagnosticReport where the DiagnosticReport.category code is a fixed LOINC as defined by the Us Core 3.1.1 DiagnosticReport Category Value Set.

Search

To retrieve clinical notes and reports, the standard FHIR search API is used.

Common client search scenarios include:

A client interested in all Radiology reports can use the following query:

GET [base]/DiagnosticReport?patient=[id]&category=http://loinc.org|LP29684-5

A client interested in all Clinical Notes can use the following query:

GET [base]/DocumentReference?patient=[id]&category=clinical-note

A client interested in all Discharge Summary Notes can use the following query:

GET [base]/DocumentReference?patient=[id]&type=http://loinc.org|18842-5

--







Developer Home





API Overview









Compliance & Certification









Implementation Guides









Ambulatory





Ambulatory Overview

Resources

Profiles

Extensions

EHI Export Guide

Capability Statement 



Endpoints 







Hospital









Azalea One









Account





About Azalea Health





Community Help Center





Sign Out

© 2025 Azalea Health, Inc.

Developer Portal

Ambulatory API Overview

Introduction

Partners may integrate with Azalea Health's Ambulatory electronic health record API platform through the power of the HL7® FHIR® Standard to build products that help patients and health care professionals.

Azalea Health's HL7® FHIR® Standard API is protected using the SMART® on FHIR® authorization framework. SMART® on FHIR® defines a profile of the OAuth 2.0 framework for obtaining authorization to act on behalf of users or systems. It is highly recommended that developers review and understand the OAuth 2.0 framework prior to implementing their authorization workflow.

SMART® vs. FHIR®

The HL7® FHIR® Standard defines an API to access information within an electronic health record system. The SMART® framework defines an API for applications to obtain an authorized context to access FHIR® resources and exchange context information with client applications.

 

Postman Collection

You can find our Azalea Ambulatory FHIR® R4 Postman Collection using the link below:

https://www.postman.com/azalea-api/workspace/azalea-ambulatory-public-api/overview

Supported Resources

You can find a full list of all resources and their corresponding interactions at the below page:

https://app.azaleahealth.com/fhir/R4/sandbox/metadata#resources

SMART® on FHIR® Configurations

You can find a full list of all supported SMART® on FHIR® Configurations at the below endpoint:

https://app.azaleahealth.com/fhir/R4/sandbox/.well-known/smart-configuration



{"authorization_endpoint":"https:\/\/app.azaleahealth.com\/fhir\/R4\/sandbox\/oauth\/authorize","token_endpoint":"https:\/\/app.azaleahealth.com\/fhir\/R4\/sandbox\/oauth\/token","token_endpoint_auth_methods_supported":["client_secret_basic"],"grant_types_supported":["authorization_code","client_credentials"],"scopes_supported":["address","email","fhirUser","launch","launch\/encounter","launch\/patient","offline_access","openid","patient\/*.*","patient\/*.read","patient\/*.write","patient\/Account.*","patient\/AllergyIntolerance.*","patient\/Appointment.*","patient\/AuditEvent.*","patient\/Binary.*","patient\/Bundle.*","patient\/CapabilityStatement.*","patient\/CarePlan.*","patient\/CareTeam.*","patient\/Claim.*","patient\/CodeSystem.*","patient\/Communication.*","patient\/Condition.*","patient\/Coverage.*","patient\/Device.*","patient\/DiagnosticReport.*","patient\/DocumentReference.*","patient\/Encounter.*","patient\/Endpoint.*","patient\/FamilyMemberHistory.*","patient\/Flag.*","patient\/Goal.*","patient\/Group.*","patient\/Immunization.*","patient\/Invoice.*","patient\/Location.*","patient\/MedicationRequest.*","patient\/MedicationStatement.*","patient\/MessageHeader.*","patient\/NamingSystem.*","patient\/Observation.*","patient\/OperationDefinition.*","patient\/Organization.*","patient\/Patient.*","patient\/PatientPortalConfiguration.*","patient\/PatientPortalEnrollment.*","patient\/PatientPortalTemplate.*","patient\/PaymentReconciliation.*","patient\/Person.*","patient\/Practitioner.*","patient\/PractitionerRole.*","patient\/Procedure.*","patient\/Provenance.*","patient\/Questionnaire.*","patient\/QuestionnaireResponse.*","patient\/RelatedPerson.*","patient\/Schedule.*","patient\/ServiceRequest.*","patient\/Slot.*","patient\/StructureDefinition.*","patient\/ValueSet.*","phone","profile","system\/*.*","system\/*.read","system\/*.write","system\/Account.*","system\/AllergyIntolerance.*","system\/Appointment.*","system\/AuditEvent.*","system\/Binary.*","system\/Bundle.*","system\/CapabilityStatement.*","system\/CarePlan.*","system\/CareTeam.*","system\/Claim.*","system\/CodeSystem.*","system\/Communication.*","system\/Condition.*","system\/Coverage.*","system\/Device.*","system\/DiagnosticReport.*","system\/DocumentReference.*","system\/Encounter.*","system\/Endpoint.*","system\/FamilyMemberHistory.*","system\/Flag.*","system\/Goal.*","system\/Group.*","system\/Immunization.*","system\/Invoice.*","system\/Location.*","system\/MedicationRequest.*","system\/MedicationStatement.*","system\/MessageHeader.*","system\/NamingSystem.*","system\/Observation.*","system\/OperationDefinition.*","system\/Organization.*","system\/Patient.*","system\/PatientPortalConfiguration.*","system\/PatientPortalEnrollment.*","system\/PatientPortalTemplate.*","system\/PaymentReconciliation.*","system\/Person.*","system\/Practitioner.*","system\/PractitionerRole.*","system\/Procedure.*","system\/Provenance.*","system\/Questionnaire.*","system\/QuestionnaireResponse.*","system\/RelatedPerson.*","system\/Schedule.*","system\/ServiceRequest.*","system\/Slot.*","system\/StructureDefinition.*","system\/ValueSet.*","user\/*.*","user\/*.read","user\/*.write","user\/Account.*","user\/AllergyIntolerance.*","user\/Appointment.*","user\/AuditEvent.*","user\/Binary.*","user\/Bundle.*","user\/CapabilityStatement.*","user\/CarePlan.*","user\/CareTeam.*","user\/Claim.*","user\/CodeSystem.*","user\/Communication.*","user\/Condition.*","user\/Coverage.*","user\/Device.*","user\/DiagnosticReport.*","user\/DocumentReference.*","user\/Encounter.*","user\/Endpoint.*","user\/FamilyMemberHistory.*","user\/Flag.*","user\/Goal.*","user\/Group.*","user\/Immunization.*","user\/Invoice.*","user\/Location.*","user\/MedicationRequest.*","user\/MedicationStatement.*","user\/MessageHeader.*","user\/NamingSystem.*","user\/Observation.*","user\/OperationDefinition.*","user\/Organization.*","user\/Patient.*","user\/PatientPortalConfiguration.*","user\/PatientPortalEnrollment.*","user\/PatientPortalTemplate.*","user\/PaymentReconciliation.*","user\/Person.*","user\/Practitioner.*","user\/PractitionerRole.*","user\/Procedure.*","user\/Provenance.*","user\/Questionnaire.*","user\/QuestionnaireResponse.*","user\/RelatedPerson.*","user\/Schedule.*","user\/ServiceRequest.*","user\/Slot.*","user\/StructureDefinition.*","user\/ValueSet.*"],"code_challenge_methods_supported":["S256"],"capabilities":["launch-standalone","launch-ehr","client-public","client-confidential-symmetric","sso-openid-connect","context-ehr-patient","context-standalone-patient","context-banner","context-style","permission-offline","permission-patient","permission-user","permission-v1"]}



Sandbox FHIR® API Endpoints

A sandbox account with test patient data is ready for you to quickly get started testing your application integration (application credentials are required).

Sandbox TypeFHIR® Base URLSandbox - FHIR® R4https://app.azaleahealth.com/fhir/R4/sandbox

Sandbox Test Users

When testing applications you can use the following user account credentials to login:

EmailPasswordUsageNotesprovider.sandbox@mailtest.azaleahealth.comsandbox1Provider appsThis user has full access to the sandbox patient population.mary.sandbox@mailtest.azaleahealth.comsandbox1Patient appsThis user is linked to two patients, Mary Imaginary and a dependent.

Change Log & Release Schedule

You can find the latest changes to the FHIR API at: https://app.azaleahealth.com/fhir/R4/changelog.

New updates to the FHIR API are generally released weekly on Wednesdays at approximately 05:00 PM EST. This schedule may change occasionally due to holidays or other factors. Be sure to check the change log each week for the latest updates.

FHIR® R4 Endpoints

Your apps can use the information found at the below page to connect to FHIR® R4 endpoints for the listed organizations:

https://app.azaleahealth.com/fhir/R4/Endpoint

--

Ambulatory Resources

The following resources are supported by the Ambulatory EHR platform:



Resource Name

Interactions & Operations

Description

Account

Search Read $class-instance

 $comment-instance

 $statement-instance

A patient level account that rolls up balance amounts from all of the patient subject's encounters. If this patient is also a guarantor (either self or for dependents) then the guarantor responsible balance can be pulled from the GuarantorAccount contained sub-Account. Each patient can have exactly one patient level financial account resource.

AllergyIntolerance

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.

Appointment

Search Create Read Update Patch $validate-resource

 $validate-instance

A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).

AuditEvent

Search Create Read $export-resource

 $validate-resource

 $validate-instance

A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.

Binary

Create Read Update Delete $validate-resource

 $validate-instance

A resource that represents the data of a single raw artifact as digital content accessible in its native format. A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.

Bundle

Search Read $office-overview-resource

A container for a collection of resources.

CapabilityStatement

Search Read

A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.

CarePlan

Search Read

Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.

CareTeam

Search Read

The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.

Claim

Search Read

A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.

CodeSystem

Search Read $find-matches-instance

The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.

Communication

Search Create Read Update Patch $read-instance

 $validate-resource

 $validate-instance

An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.

Condition

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.

Coverage

Search Create Read Update Patch $validate-resource

 $validate-instance

Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.

Device

Search Read

A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.

DiagnosticReport

Search Read

The findings and interpretation of diagnostic tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.

DocumentReference

Search Create Read Update Patch $docref-resource

 $validate-resource

 $validate-instance

A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.

Encounter

Search Create Read Update Patch $class-instance

 $comment-instance

 $copy-instance

 $download-resource

 $download-instance

 $print-resource

 $print-instance

 $transcribe-instance

 $transmit-resource

 $transmit-instance

 $validate-resource

 $validate-instance

An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.

Endpoint

Search Read

The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.

FamilyMemberHistory

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

Significant health conditions for a person related to the patient relevant in the context of care for the patient.

Flag

Search Read

Prospective warnings of potential issues when providing care to the patient.

Goal

Search Read

Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.

Group

Search Read $export-instance

Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.

Immunization

Search Read

Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.

Invoice

Search Read $adjustment-instance

 $class-instance

 $comment-instance

 $refund-instance

Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.

Location

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.

MedicationRequest

Search Read

An order or request for both supply of the medication and the instructions for administration of the medication to a patient.

MedicationStatement

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

This profile covers the 'No Known Medications' (NKM) indication.

MessageHeader

Search Read

The header for a message exchange that is either requesting or responding to an action.

NamingSystem

Search Read

A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc. Represents a "System" used within the Identifier and Coding data types.

Observation

Search Create Read Update Patch Delete $lastn-resource

 $validate-resource

 $validate-instance

Observations are a central element in healthcare, used to support diagnosis, monitor progress, determine baselines and patterns and even capture demographic characteristics. Most observations are simple name/value pair assertions with some metadata, but some observations group other observations together logically, or even are multi-component observations. Note that the DiagnosticReport resource provides a clinical or workflow context for a set of observations and the Observation resource is referenced by DiagnosticReport to represent laboratory, imaging, and other clinical and diagnostic data to form a complete report.

OperationDefinition

Search Read

A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).

Organization

Search Read

A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.

Patient

Search Create Read Update Patch Delete $class-instance

 $download-instance

 $export-resource

 $merge-resource

 $transmit-instance

 $validate-resource

 $validate-instance

Demographics and other administrative information about an individual or animal receiving care or other health-related services.

PaymentReconciliation

Search Create Read Delete $refund-instance

 $validate-resource

 $validate-instance

This resource provides the details including amount of a payment and allocates the payment items being paid.

Person

Search Read

Demographics and administrative information about a person independent of a specific health-related context.

Practitioner

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

A person who is directly or indirectly involved in the provisioning of healthcare.

PractitionerRole

Search Read

A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.

Procedure

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.

Provenance

Search Read

Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource.

Questionnaire

Search Read

A set of one or more structured questions (such as a survey) that can be embedded as a clinical note on an Encounter. Note that evaluation tables do not support nested or grouped questions.

QuestionnaireResponse

Search Create Read Update Patch Delete $validate-resource

 $validate-instance

A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.

RelatedPerson

Search Create Read Update Patch $validate-resource

 $validate-instance

Information about a person that is involved in a patient's health or the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.

Schedule

Search Read

A container for slots of time that may be available for booking appointments.

ServiceRequest

Search Read

A record of a request for service such as diagnostic investigations, treatments, or " . "operations to be performed.

Slot

Search Read

A slot of time on a schedule that may be available for booking appointments.

StructureDefinition

Search Read

A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.

ValueSet

Search Read $expand-instance

 $expand-resource

A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context.

--

Ambulatory Profiles

The following custom profiles are defined by the Ambulatory EHR platform:



Profile Name

Resource Type

Description

Account

Account

A financial tool for tracking value accrued for a particular purpose. In the healthcare field, used to track charges for a patient, cost centers, etc.

AllergyIntolerance

AllergyIntolerance

Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.

Appointment

Appointment

A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).

AuditEvent

AuditEvent

A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.

Bundle

Bundle

A container for a collection of resources.

CarePlan

CarePlan

Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.

CareTeam

CareTeam

The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.

Communication

Communication

An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.

Condition

Condition

A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.

Coverage

Coverage

Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.

Device

Device

A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.

DiagnosticReport

DiagnosticReport

The findings and interpretation of diagnostic tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.

DocumentReference

DocumentReference

A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.

EmploymentStatus

Observation

This profile sets minimum expectations for the Observation resource to record, search, and fetch employment status observations associated with a patient.

Encounter

Encounter

An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.

EncounterAccount

Account

An encounter level account (or charge group) that accrues a balance amount for a single encounter. Each encounter can have exactly one encounter level charge group account resource.

EncounterDiagnosis

Condition

A point in time encounter diagnosis for a given Encounter. The Condition.category code must be 'encounter-diagnosis'.

Endpoint

Endpoint

The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.

EvaluationTable

Questionnaire

A set of one or more structured questions (such as a survey) that can be embedded as a clinical note on an Encounter. Note that evaluation tables do not support nested or grouped questions.

EvaluationTableAnswer

QuestionnaireResponse

A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.

FamilyMemberHistory

FamilyMemberHistory

Significant health conditions for a person related to the patient relevant in the context of care for the patient.

Goal

Goal

Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.

Group

Group

Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.

Immunization

Immunization

Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.

Invoice

Invoice

Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.

Location

Location

Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.

MedicationRequest

MedicationRequest

An order or request for both supply of the medication and the instructions for administration of the medication to a patient.

MedicationStatement

MedicationStatement

A record of a medication that is being consumed by a patient. A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future. The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician. A common scenario where this information is captured is during the history taking process during a patient visit or stay. The medication information may come from sources such as the patient's memory, from a prescription bottle, or from a list of medications the patient, clinician or other party maintains.

MessageHeader

MessageHeader

The header for a message exchange that is either requesting or responding to an action.

NoKnownAllergies

AllergyIntolerance

This profile covers the 'No Known Allergies' (NKA) indication.

NoKnownMedications

MedicationStatement

This profile covers the 'No Known Medications' (NKM) indication.

Observation

Observation

Observations are a central element in healthcare, used to support diagnosis, monitor progress, determine baselines and patterns and even capture demographic characteristics. Most observations are simple name/value pair assertions with some metadata, but some observations group other observations together logically, or even are multi-component observations. Note that the DiagnosticReport resource provides a clinical or workflow context for a set of observations and the Observation resource is referenced by DiagnosticReport to represent laboratory, imaging, and other clinical and diagnostic data to form a complete report.

Organization

Organization

A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.

Patient

Patient

Demographics and other administrative information about an individual or animal receiving care or other health-related services.

PatientAccount

Account

A patient level account that rolls up balance amounts from all of the patient subject's encounters. If this patient is also a guarantor (either self or for dependents) then the guarantor responsible balance can be pulled from the GuarantorAccount contained sub-Account. Each patient can have exactly one patient level financial account resource.

PatientAllergy

AllergyIntolerance

This profile covers patient allergies with the exception of 'No Known drug allergies'.

PatientProblem

Condition

A patient problem list item that appears in the patient's problem history. The Condition.category code must be 'problem-list-item'.

PaymentReconciliation

PaymentReconciliation

This resource provides the details including amount of a payment and allocates the payment items being paid.

Practitioner

Practitioner

A person who is directly or indirectly involved in the provisioning of healthcare.

PractitionerRole

PractitionerRole

A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.

Procedure

Procedure

An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.

Questionnaire

Questionnaire

A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.

QuestionnaireResponse

QuestionnaireResponse

A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.

Recall

CarePlan

Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.

RelatedPerson

RelatedPerson

Information about a person that is involved in a patient's health or the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.

Schedule

Schedule

A container for slots of time that may be available for booking appointments.

Slot

Slot

A slot of time on a schedule that may be available for booking appointments.

SmokingStatus

Observation

This profile sets minimum expectations for the Observation resource to record, search, and fetch smoking status data associated with a patient.

SocialHistoryQuestion

Questionnaire

Represents a single social history question.

TravelHistory

Observation

This profile sets minimum expectations for the Observation resource to record, search, and fetch travel history observations associated with a patient.

UnappliedPayment

PaymentReconciliation

This resource provides the details including amount of a payment and allocates the payment items being paid.

--

Ambulatory Extensions

The following extensions are defined and supported by the Ambulatory EHR platform:



Extension Name

Publisher

Description

Account Aging

Azalea Health, Inc.

Aging buckets for an account balance.

Account Balance Amount

Azalea Health, Inc.

Balance amount after all other payments and adjustments are taken into account.

Account Location Id

Azalea Health, Inc.

Location id of visit where balances were incurred.

Account Patient Links

Azalea Health, Inc.

Linked patients along with their balance information.

Account Related Parts

Azalea Health, Inc.

A reference to other related Accounts.

Account Status

Azalea Health, Inc.

The status of the Account within the billing workflow.

Account Unapplied Amount

Azalea Health, Inc.

The amount of any unapplied money or credits on the account.

Account Visit Date

Azalea Health, Inc.

Visit or encounter dates where balances were incurred.

Account Visit Id

Azalea Health, Inc.

Visit or encounter id where balances were incurred.

Allergy category SNOMED-CT coding

Azalea Health, Inc.

This describes the type of product and intolerance suffered by the patient.

Allergy severity SNOMED-CT coding

Azalea Health, Inc.

A value set of SNOMED-CT codes reflecting the level of the severity of an allergy or intolerance.

Appointment Reason Color

Azalea Health, Inc.

Appointment Reason Color

Appointment Reminder Eligibility

Azalea Health, Inc.

Appointment Reminder Eligibility

Appointment Reminder Status

Azalea Health, Inc.

Appointment Reminder Status

Appointment Requested State

Azalea Health, Inc.

Appointment Requested State

Appointment Status History

Azalea Health, Inc.

Appointment Status History

Billing Code

Azalea Health, Inc.

A billing or transaction code.

ChargeItem Note

Azalea Health, Inc.

A note added to a ChargeItem.

Claim Insurance Referral

Azalea Health, Inc.

Contains insurance referral data.

Claim Item Authorization Number

Azalea Health, Inc.

Claim Item Authorization Number.

Claim Item NDC Quantity

Azalea Health, Inc.

NDC Quantity for a Claim Item.

Claim Item Not Otherwise Classified (NOC)

Azalea Health, Inc.

Additional Claim Documentation Requirements for Not Otherwise Classified (NOC).

Claim Third Party Liability

Azalea Health, Inc.

Contains insurance third party liability code and status.

Coding RxNorm Term Type (TTY) Code

Azalea Health, Inc.

SAB=RXNORM uses term types (TTYs) to indicate generic and branded drug names at different levels of specificity.

Communication Read Flag

Azalea Health, Inc.

Whether the communication was read by the authenticated user.

Coverage Medicare Secondary Reason Code

Azalea Health, Inc.

Coverage Medicare Secondary Reason Code

Coverage Note

Azalea Health, Inc.

Coverage Note

Coverage Vaccines Covered

Azalea Health, Inc.

Coverage Vaccines Covered

DocumentReference Label

Azalea Health, Inc.

A label for this document.

Education Provided

Azalea Health, Inc.

Whether or not education materials were provided for this resource item.

Encounter Class

Azalea Health, Inc.

Azalea Ambulatory custom defined encounter classes.

Encounter Note

Azalea Health, Inc.

Encounter Note

Encounter Signature Extension

Azalea Health, Inc.

Encounter Signature Extension

Encounter Status

Azalea Health, Inc.

Azalea Ambulatory status codes for encounter status.

Guarantor Linked Patient

Azalea Health, Inc.

Guarantor Linked Patient

Invoice Line Item Adjustments

Azalea Health, Inc.

The total adjustment amount for a line item.

Invoice Line Item Charges

Azalea Health, Inc.

The total charge amount for a line item.

Invoice Line Item Payments

Azalea Health, Inc.

The total payment amount for a line item.

Invoice Line Item Subtotal

Azalea Health, Inc.

The sub-total amount for a line item.

Invoice Next Payer

Azalea Health, Inc.

The next payer for a balance amount.

Invoice Price Component Date

Azalea Health, Inc.

The date that a price component line item payment or adjustment posted.

Invoice Price Component Identifier

Azalea Health, Inc.

An external identifier for a price component line item payment or adjustment.

Invoice Price Component Payer

Azalea Health, Inc.

The payer for a price component line item payment or adjustment.

Invoice Visit Date

Azalea Health, Inc.

Visit or encounter dates where balances were incurred.

Invoice Visit Id

Azalea Health, Inc.

Visit or encounter id where balances were incurred.

Location Reference

Azalea Health, Inc.

A reference to a Location resource.

Patient Citizenship

The patient's legal status as citizen of a country.

Patient Class

Azalea Health, Inc.

Azalea Ambulatory custom defined patient classes.

Patient Contact Birth Date

Azalea Health, Inc.

The birth date of a patient contact.

Patient Default Location

Azalea Health, Inc.

The default location to apply to encounters for a patient.

Patient Employment Status

Azalea Health, Inc.

Patient Employment Status

Patient Incomplete Status

Azalea Health, Inc.

Patient Incomplete Status

Patient Occupation

Azalea Health, Inc.

The patients occupation for a given employer contact.

Patient Popup Group

Azalea Health, Inc.

Patient Popup Group

Patient Preferred Contact Method

Azalea Health, Inc.

The patient preferred contact method as represented in Azalea Ambulatory.

Patient Reference

Azalea Health, Inc.

A reference to a Patient resource.

Patient Religion

The patient's professed religious affiliations.

Patient annual income

Azalea Health, Inc.

Patient annual income

Patient household members

Azalea Health, Inc.

Patient household members

Payment Reconciliation Apply To Encounter

Azalea Health, Inc.

The Encounter intended for the payment.

PaymentReconciliation Gateway

Azalea Health, Inc.

Settlement details from a connected payment gateway.

Procedure Charge Item Reference

Azalea Health, Inc.

A reference to a Charge Item associated with this Procedure (can be contained).

Related Person Employer

Azalea Health, Inc.

Related Person Employer

Room Flag

Azalea Health, Inc.

Room Flag

Room Max Occupancy

Azalea Health, Inc.

Room Max Occupancy

Schedule End Time

Azalea Health, Inc.

The daily end time for the schedule.

Schedule Insurance

Azalea Health, Inc.

Limits a Schedule to a particular insurance payer.

Schedule Insurance Class

Azalea Health, Inc.

Limits a Schedule to a particular insurance class.

Schedule Slot Interval

Azalea Health, Inc.

The slot interval for the schedule.

Schedule Start Time

Azalea Health, Inc.

The daily start time for the schedule.

--

Ambulatory EHI Export Guide

Introduction

For additional implementation details please see the §170.315 (b)(10) EHI Export overview guide.

Resource Data Mappings

The following EHR concepts are exported to the given FHIR Resource(s):



EHR Concept

FHIR Resource

Notes

Allergies

AllergyIntolerance

Appointments

Appointment

Care Plans

CarePlan

Care Plans (Goals)

Goal

Care Teams

CareTeam

Chart Evaluation Tables (Answers)

QuestionnaireResponse

Chart Plan Note

DocumentReference

DocumentReference.where(type = "11506-3")

Chart Procedure Note

DocumentReference

DocumentReference.where(type = "28570-0")

Chart Subjective (PMH) Note

DocumentReference

DocumentReference.where(type = "34117-2")

Documents

DocumentReference

Encounter (Billing)

Claim

Claim.where(use = "claim")

Encounter (Clinical)

Encounter

Encounter Diagnoses

Condition

Condition.where(category.coding.code = "encounter-diagnosis")

Encounter Financial Account

Account

Account.where(type.text = "charge-group")

Encounter Procedures

Procedure

Family History

FamilyMemberHistory

Health Concerns

Condition

Condition.where(category.coding.code = "health-concern")

Immunizations

Immunization

Implantable Devices

Device

Insurance

Coverage

Laboratory Orders

ServiceRequest

Laboratory Reports

DiagnosticReport

Laboratory Results

Observation

Observation.where(category.coding.code = "laboratory)

Locations

Location

Medications

MedicationStatement

Patient Classes

Group

Group.where(code.text = "patient-group")

Patient Comments

Flag

Flag.where(category.text = "patient-comment")

Patient Demographics

Patient

Patient Documents

DocumentReference

Patient Emergency Contact

Patient

Patient.contact.where(relationship.code = "C")

Patient Employer

Patient

Patient.contact.where(relationship.code = "E")

Patient Employment Status

Observation

Observation.where(code.coding.code = "224362002")

Patient Financial Account

Account

Account.where(type.text = "financial-account")

Patient Guarantor

RelatedPerson

RelatedPerson.where(relationship.code = "GUAR")

Patient Handouts

DocumentReference

DocumentReference.where(type.coding.code = "51855-5")

Patient Next of Kin

Patient

Patient.contact.where(relationship.code = "next-of-kin")

Patient Popup Comments

Flag

Flag.where(category.text = "patient-popup")

Patient Portal Messages

Communication

Communication.where(sender.type = "Patient") or Communication.where(recipient.type = "Patient")

Patient Power of Attorney

RelatedPerson

RelatedPerson.where(relationship.code = "GUARD")

Patient Statements

Invoice

Patient Travel History

Observation

Observation.where(code.coding.code = "443846001")

Patient Urls

DocumentReference

DocumentReference.where(type.coding.code = "51899-3")

Payments (Applied + Unapplied)

PaymentReconciliation

Pre-Certifications

Claim

Claim.where(use = "preauthorization")

Prescriptions

MedicationRequest

Problem History

Condition

Condition.where(category.coding.code = "patient-problem-list")

Procedure History

Procedure

Providers

Practitioner

Radiology Orders

ServiceRequest

Radiology Reports

DiagnosticReport

Radiology Results

Observation

Observation.where(category.coding.code = "laboratory)

Recalls

CarePlan

CarePlan.where(category.text = "recall")

Sexual Orientation

Observation

Observation.where(code.coding.code = "76690-7")

Smoking Status

Observation

Observation.where(code.coding.code = "72166-2")

Social History

Observation

Observation.where(category.coding.code = "social-history)

Social Questions (Answers)

QuestionnaireResponse

Vital Signs

Observation

Observation.where(category.coding.code = "vital-signs)

--

Capability Statement

Partners may integrate with Azalea Health's electronic health record API platform through the power of the HL7® FHIR® Standard to build products that help patients and health care professionals. FHIR is a standard for health care data exchange, published by HL7®. For more details about FHIR, please refer to the official specification.

This document describes the FHIR API capabilities for the Azalea Ambulatory software platform. To view all supported software platforms please visit our Developer Portal home page.



Details

Software NameAzalea AmbulatoryFHIR Version4.0.1Publication StatusactiveLast Changed2025-03-24Build Version:40257Published ByAzalea Health, Inc.URLhttps://app.azaleahealth.com/fhir/R4/CapabilityStatement/R4Formatsapplication/fhir+json

application/fhir+xml

Patch Formatsapplication/json-patch+json

Go to StructureDefinition List



RESTful Interface

Security

Azalea Health's HL7® FHIR® Standard API is protected using the SMART® on FHIR® authorization framework. SMART® on FHIR® defines a profile of the OAuth 2.0 framework for obtaining authorization to act on behalf of users or systems. It is highly recommended that developers review and understand the OAuth 2.0 framework prior to implementing their authorization workflow.

CORS SupportYesServiceSMART-on-FHIR

Resources

FHIR is based on "Resources" which are the common building blocks for all exchanges. Resources are an instance-level representation of some kind of healthcare entity. The following resources are supported by this server instance:

Resource NameInteractionsResource DescriptionAccountsearch-type readA patient level account that rolls up balance amounts from all of the patient subject's encounters. If this patient is also a guarantor (either self or for dependents) then the guarantor responsible balance can be pulled from the GuarantorAccount contained sub-Account. Each patient can have exactly one patient level financial account resource.AllergyIntolerancesearch-type create read update patch deleteRisk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.Appointmentsearch-type create read update patchA booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).AuditEventsearch-type create readA record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.Binarycreate read update deleteA resource that represents the data of a single raw artifact as digital content accessible in its native format. A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.Bundlesearch-type readA container for a collection of resources.CapabilityStatementsearch-type readA Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.CarePlansearch-type readDescribes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.CareTeamsearch-type readThe Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.Claimsearch-type readA provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.CodeSystemsearch-type readThe CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.Communicationsearch-type create read update patchAn occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.Conditionsearch-type create read update patch deleteA clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.Coveragesearch-type create read update patchFinancial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.Devicesearch-type readA type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.DiagnosticReportsearch-type readThe findings and interpretation of diagnostic tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.DocumentReferencesearch-type create read update patchA reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.Encountersearch-type create read update patchAn interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.Endpointsearch-type readThe technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.FamilyMemberHistorysearch-type create read update patch deleteSignificant health conditions for a person related to the patient relevant in the context of care for the patient.Flagsearch-type readProspective warnings of potential issues when providing care to the patient.Goalsearch-type readDescribes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.Groupsearch-type readRepresents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.Immunizationsearch-type readDescribes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.Invoicesearch-type readInvoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.Locationsearch-type create read update patch deleteDetails and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.MedicationRequestsearch-type readAn order or request for both supply of the medication and the instructions for administration of the medication to a patient.MedicationStatementsearch-type create read update patch deleteThis profile covers the 'No Known Medications' (NKM) indication.MessageHeadersearch-type readThe header for a message exchange that is either requesting or responding to an action.NamingSystemsearch-type readA curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc. Represents a "System" used within the Identifier and Coding data types.Observationsearch-type create read update patch deleteObservations are a central element in healthcare, used to support diagnosis, monitor progress, determine baselines and patterns and even capture demographic characteristics. Most observations are simple name/value pair assertions with some metadata, but some observations group other observations together logically, or even are multi-component observations. Note that the DiagnosticReport resource provides a clinical or workflow context for a set of observations and the Observation resource is referenced by DiagnosticReport to represent laboratory, imaging, and other clinical and diagnostic data to form a complete report.OperationDefinitionsearch-type readA formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).Organizationsearch-type readA formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.Patientsearch-type create read update patch deleteDemographics and other administrative information about an individual or animal receiving care or other health-related services.PaymentReconciliationsearch-type create read deleteThis resource provides the details including amount of a payment and allocates the payment items being paid.Personsearch-type readDemographics and administrative information about a person independent of a specific health-related context.Practitionersearch-type create read update patch deleteA person who is directly or indirectly involved in the provisioning of healthcare.PractitionerRolesearch-type readA specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.Proceduresearch-type create read update patch deleteAn action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.Provenancesearch-type readProvenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource.Questionnairesearch-type readA set of one or more structured questions (such as a survey) that can be embedded as a clinical note on an Encounter. Note that evaluation tables do not support nested or grouped questions.QuestionnaireResponsesearch-type create read update patch deleteA structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.RelatedPersonsearch-type create read update patchInformation about a person that is involved in a patient's health or the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.Schedulesearch-type readA container for slots of time that may be available for booking appointments.ServiceRequestsearch-type readA record of a request for service such as diagnostic investigations, treatments, or " . "operations to be performed.Slotsearch-type readA slot of time on a schedule that may be available for booking appointments.StructureDefinitionsearch-type readA definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.ValueSetsearch-type readA ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context.

© Copyright 2025 Azalea Health, Inc..

--

FHIR R4 Endpoints

Your applications can use the information below to connect to FHIR R4 endpoints for the listed organizations.

ID:  Name:   Active only



Download as a FHIR JSON Bundle



Organization Name | Status| Location | FHIR R4 Base URL | COMPREHENSIVE MEDICAL CLINIC LLC | active | NORCROSS, GA | https://app.azaleahealth.com/fhir/R4/142219

--

Connected Apps







 Connected AppsApplication Details





 This application is owned and maintained by Azalea Health. For support, please visit our help site.

Name

Azalea Ambulatory

Description

Azalea Health’s cloud based Ambulatory EHR.

Ownership

Azalea Health

Website

https://www.azaleahealth.com

Sign In

https://app.azaleahealth.com/login.php?sso

--

Azalea Ambulatory Public API





Partners may integrate with Azalea Health's Ambulatory electronic health record API platform through the power of the HL7® FHIR® Standard to build products that help patients and health care professionals.

Azalea Health's HL7® FHIR® Standard API is protected using the SMART® on FHIR® authorization framework. SMART® on FHIR® defines a profile of the OAuth 2.0 framework for obtaining authorization to act on behalf of users or systems. It is highly recommended that developers review and understand the OAuth 2.0 framework prior to implementing their authorization workflow.

SMART® vs. FHIR®

The HL7® FHIR® Standard defines an API to access information within an electronic health record system. The SMART® framework defines an API for applications to obtain an authorized context to access FHIR® resources and exchange context information with client applications.

Sandbox

A sandbox account with test patient data is ready for you to quickly get started testing your application integration. Application credentials are required to get started. Please review the instructions for registering an application.

Authorization

The easiest way to get started testing is to create an application that is enabled for client_credentials access. Provide the following configurations in the application details page of the Azalea Health Developer Portal:

For the "Client authentication" field select Confidential client.

The SMART® Backend Services Authorization field must be checked.

You must pre-authorize all scopes via the SMART® Backend Authorization Scopes text field. You can enter system/\\\\\*.\\\\\* for all access.

Once this is done take note of the Client ID and Client Secret values for the Ambulatory Sandbox.

In the "Sandbox" Postman environment fill in these values for the respective client_id and client_secret variables as the "Current Value". Make sure that this environment is selected in the top-right hand corner drop down. If you chose to pre-authorize scopes other than system/\\\\\*.\\\\\* in step 3 above then you should modify the current value for the client_credentials_scopes variable.

Get an access token

You must obtain an access token in order to make requests. Open the "FHIR R4 API" collection and select the "Authorization" section. It should be pre-loaded for OAuth2 Client Credentials authorization. If you filled in your client_id, client_secret , and client_credentials_scopes environment variables correctly then you can press the "Get New Access Token" button to authorize. Now you can start making requests!

Sandbox Test Users

When testing standalone applications you can use the following user account credentials to login:

Mary Imaginary

Email: mary.sandbox@mailtest.azaleahealth.com

Password: sandbox1

Usage: Patient apps

This user is linked to two patients, self and a dependent.

Provider Sandbox, M.D.

Email: provider.sandbox@mailtest.azaleahealth.com﻿

Password: sandbox1

Usage: Provider apps

This user has full access to the sandbox patient population.







--------







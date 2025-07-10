Translation Microservice
A lightweight, modular translation microservice built with FastAPI that provides text translation capabilities. The service currently uses a mock translation API but can be easily configured to use the Google Translate API for production use.

Features
Single text translation (up to 1000 characters) via POST request
Bulk translation support for multiple texts in one request
Support for multiple target languages (ISO codes)
Input validation and error handling
Comprehensive logging of all translation requests to SQLite database
Health check endpoint for monitoring service status
Modular code structure for easy maintenance and extension



## Screenshots

### API Documentation
![API Documentation](app/Screenshot%202025-07-11%20005904.png)

### Translation Example
![Translation Example](app/Screenshot%202025-07-11%20010045.png)

Project Structure
plaintext

├── app/│   ├── __init__.py│   ├── db/│   │   ├── __init__.py│   │   └── database.py         # SQLite database operations│   ├── main.py                 # Application entry point│   ├── models/│   │   ├── __init__.py│   │   └── schemas.py          # Pydantic models for requests/responses│   ├── routes/│   │   ├── __init__.py│   │   ├── health.py           # Health check endpoint│   │   └── translation.py      # Translation endpoints│   ├── services/│   │   ├── __init__.py│   │   └── translator.py       # Translation service implementation│   └── utils/│       ├── __init__.py│       └── logger.py           # Logging utilities├── requirements.txt            # Project dependencies├── translation_logs.db         # SQLite database for logs└── translation_service.log     # Application log file
Prerequisites
Python 3.8 or higher
pip (Python package installer)
Installation
Clone the repository or download the source code

Navigate to the project directory:

bash
Run
cd "path\to\translation-microservice"
Install the required dependencies:

bash
Run
pip install -r requirements.txt
If you encounter permission issues:

bash
Run
pip install --user -r requirements.txt
Running the Service
Start the FastAPI server:

bash
Run
python -m uvicorn app.main:app --reload
The server will start on http://127.0.0.1:8000 by default.

To verify the service is running, access the API documentation at:

plaintext

http://127.0.0.1:8000/docs
API Endpoints
1. Health Check
Endpoint: GET /health

Description: Check if the service is running properly

Example (PowerShell):

powershell
Run
Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -Method Get
Response:

json

{  "status": "healthy",  "version": "1.0.0",  "timestamp":   "2023-11-15T12:34:56.789012"}
2. Single Text Translation
Endpoint: POST /api/v1/translate

Description: Translate a single text to the specified target language

Request Body:

json

{  "text": "hello",  "target_language": "hi"}
Example (PowerShell):

powershell
Run
$body = @{ text = "hello"; target_language = "hi" } | ConvertTo-JsonInvoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/translate" -Method Post -Body $body -ContentType "application/json"
Response:

json

{  "original_text": "hello",  "translated_text": "नमस्ते",  "target_language": "hi"}
3. Bulk Translation
Endpoint: POST /api/v1/translate/bulk

Description: Translate multiple texts to the specified target language

Request Body:

json

{  "texts": ["hello", "thank   you", "goodbye"],  "target_language": "hi"}
Example (PowerShell):

powershell
Run
$body = @{     texts = @("hello", "thank     you", "goodbye");     target_language = "hi" } | ConvertTo-JsonInvoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/translate/bulk" -Method Post -Body $body -ContentType "application/json"
Response:

json

{  "translations": [    {      "original_text":       "hello",      "translated_text":       "नमस्ते",      "target_language": "hi"    },    {      "original_text": "thank       you",      "translated_text":       "धन्यवाद",      "target_language": "hi"    },    {      "original_text":       "goodbye",      "translated_text":       "अलविदा",      "target_language": "hi"    }  ]}
Supported Languages
The mock translation service currently supports these languages:

Hindi (hi)
Tamil (ta)
Kannada (kn)
Bengali (bn)
The mock service only has translations for these phrases:

"hello"
"how are you"
"thank you"
"goodbye"
For any other text, the service will return the original text with the language code prefix, e.g., [hi] Your text here.

Using Real Google Translate API
To use the actual Google Translate API instead of the mock:

Uncomment the relevant code in app/services/translator.py
Install the required Google Translate package (already in requirements.txt)
Restart the service
Logging
The service logs all translation requests to:

Console output
translation_service.log file
SQLite database (translation_logs.db)
Error Handling
The API includes validation for:

Text length (maximum 1000 characters)
Language code format
Empty requests
Errors are returned with appropriate HTTP status codes and descriptive messages.

Development
Running Tests
bash
Run
# To be implementedpython -m pytest
Adding New Features
The modular structure makes it easy to extend the service:

Add new routes in the app/routes/ directory
Extend models in app/models/schemas.py
Add new services in the app/services/ directory
Troubleshooting
Common Issues
Server won't start

Check if the port is already in use
Verify all dependencies are installed
Check for syntax errors in the code
Translation not working

Remember that the mock service only translates specific phrases
Check the language code is supported
Verify the request format is correct
Connection errors

Ensure the server is running
Check if you're using the correct URL and port
Verify network connectivity
License
MIT

Created with FastAPI and Python 3.x

### Translation Microservice
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


### Prerequisites
Python 3.8 or higher
pip (Python package installer)
Installation
Clone the repository or download the source code

Navigate to the project directory:

cd "path\to\translation-microservice"
Install the required dependencies:


pip install -r requirements.txt
If you encounter permission issues:

pip install --user -r requirements.txt
Running the Service
Start the FastAPI server:

python -m uvicorn app.main:app --reload

The server will start on http://127.0.0.1:8000 by default.

To verify the service is running, access the API documentation at:

http://127.0.0.1:8000/docs


### API Endpoints


### 1. Health Check
Endpoint: GET /health
Description: Check if the service is running properly

Example (PowerShell):

Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -Method Get
Response:

json
{  "status": "healthy",  "version": "1.0.0",  "timestamp":   "2023-11-15T12:34:56.789012"}


### 2. Single Text Translation
Endpoint: POST /api/v1/translate

Description: Translate a single text to the specified target language

Request Body:
json

{  "text": "hello",  "target_language": "hi"}
Example (PowerShell):

$body = @{ text = "hello"; target_language = "hi" } | ConvertTo-JsonInvoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/translate" -Method Post -Body $body -ContentType "application/json"
Response:

json

{  "original_text": "hello",  "translated_text": "नमस्ते",  "target_language": "hi"}


###3. Bulk Translation
Endpoint: POST /api/v1/translate/bulk

Description: Translate multiple texts to the specified target language

Request Body:

json

{  "texts": ["hello", "thank   you", "goodbye"],  "target_language": "hi"}
Example (PowerShell):


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
French (fre)
The mock service only has translations for these phrases:

"hello"
"how are you"
"thank you"
"goodbye"
For any other text, the service will return the original text with the language code prefix, e.g., [hi] Your text here.


Created with FastAPI and Python 3.x

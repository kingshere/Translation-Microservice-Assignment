### Translation Microservice
A lightweight, modular, and scalable translation microservice built with FastAPI to provide text translation capabilities. The service currently uses a mock translation system but is designed to integrate seamlessly with the Google Translate API for production use. It supports single and bulk text translations, comprehensive logging, and a health check endpoint for monitoring.
Features

Single Text Translation: Translate a single text (up to 1000 characters) to a specified target language via a POST request.
Bulk Translation: Translate multiple texts in a single request.
Supported Languages: Mock translations for Hindi (hi), Tamil (ta), Kannada (kn), Bengali (bn), and French (fre).
Input Validation: Robust validation using Pydantic to ensure valid inputs.
Logging: Logs all translation requests to an SQLite database and a file for auditing and debugging.
Health Check: Endpoint to monitor service status.
Modular Design: Organized code structure for easy maintenance and extensibility.

### Prerequisites

Python: 3.8 or higher
pip: Python package installer
A working internet connection (for dependency installation)

### Running the Service

Start the FastAPI Server:
python -m uvicorn app.main:app --reload

The service will run on http://127.0.0.1:8000 by default.

Access API Documentation:Open your browser and navigate to:
http://127.0.0.1:8000/docs

This provides an interactive Swagger UI for testing the API.


### API Endpoints
### 1. Health Check

Endpoint: GET /health
Description: Verifies the service is running.
Response:{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-07-12T02:05:00.123456"
}


Example (cURL):curl http://127.0.0.1:8000/health



### 2. Single Text Translation

Endpoint: POST /api/v1/translate
Description: Translates a single text to the specified target language.
Request Body:{
  "text": "hello",
  "target_language": "hi"
}


Response:{
  "original_text": "hello",
  "translated_text": "नमस्ते",
  "target_language": "hi"
}


Example (cURL):curl -X POST http://127.0.0.1:8000/api/v1/translate -H "Content-Type: application/json" -d '{"text":"hello","target_language":"hi"}'



### 3. Bulk Translation

Endpoint: POST /api/v1/translate/bulk
Description: Translates multiple texts to the specified target language.
Request Body:{
  "texts": ["hello", "thank you", "goodbye"],
  "target_language": "hi"
}


Response:{
  "translations": [
    {
      "original_text": "hello",
      "translated_text": "नमस्ते",
      "target_language": "hi"
    },
    {
      "original_text": "thank you",
      "translated_text": "धन्यवाद",
      "target_language": "hi"
    },
    {
      "original_text": "goodbye",
      "translated_text": "अलविदा",
      "target_language": "hi"
    }
  ]
}


Example (cURL):curl -X POST http://127.0.0.1:8000/api/v1/translate/bulk -H "Content-Type: application/json" -d '{"texts":["hello","thank you","goodbye"],"target_language":"hi"}'



### Supported Languages
The mock translation service supports the following languages:

Hindi (hi)
Tamil (ta)
Kannada (kn)
Bengali (bn)
French (fre)

Note: The mock service only translates the following phrases:

"hello"
"how are you"
"thank you"
"goodbye"

For unsupported texts, the service returns the original text prefixed with the language code (e.g., [hi] some text).


### Logging

Database: Translation requests are logged to translation_logs.db with fields: source_text, target_language, translated_text, and timestamp.
File: Request and response details are logged to translation_service.log for debugging.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

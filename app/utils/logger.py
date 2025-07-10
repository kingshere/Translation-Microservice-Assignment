import logging
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("translation_service.log")
    ]
)

logger = logging.getLogger("translation-service")

def log_request(request_data, response_data=None, error=None):
    """Log request and response information"""
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "request": request_data,
    }
    
    if response_data:
        log_data["response"] = response_data
    
    if error:
        log_data["error"] = str(error)
        logger.error(f"Translation error: {log_data}")
    else:
        logger.info(f"Translation request: {log_data}")
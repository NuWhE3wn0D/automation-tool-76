import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

def process_payload(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if data is None:
        logger.error("Received null payload")
        raise ProcessingError("Payload cannot be null")
    
    if not isinstance(data, dict):
        logger.error("Invalid payload type: %s", type(data).__name__)
        raise ProcessingError("Payload must be a dictionary")
    
    try:
        result = {}
        for key, value in data.items():
            if not isinstance(key, str):
                raise ValueError(f"Key {key} must be a string")
            result[key] = str(value).strip()
        return result
    except Exception as e:
        logger.exception("Unexpected error during payload processing")
        raise ProcessingError(f"Failed to process payload: {e}") from e

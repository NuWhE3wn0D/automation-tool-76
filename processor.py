import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ProcessingError(Exception):
    pass


class InvalidPayloadError(ProcessingError):
    pass


class TaskProcessor:
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries

    def parse_payload(self, raw_data: str) -> Dict[str, Any]:
        if not raw_data or not raw_data.strip():
            raise InvalidPayloadError("Payload cannot be empty")
        try:
            data = json.loads(raw_data)
            if not isinstance(data, dict):
                raise InvalidPayloadError("Payload must be a JSON object")
            return data
        except json.JSONDecodeError as err:
            raise InvalidPayloadError(f"Invalid JSON syntax: {err}") from err

    def process_task(self, raw_data: str) -> Optional[Dict[str, Any]]:
        try:
            payload = self.parse_payload(raw_data)
            action = payload.get("action")
            if not action or not isinstance(action, str):
                raise InvalidPayloadError("Missing or invalid 'action' key")

            params = payload.get("params", {})
            if not isinstance(params, dict):
                raise InvalidPayloadError("'params' must be a dictionary")

            return {"status": "success", "action": action, "result": params}
        except InvalidPayloadError as err:
            logger.error("Payload processing failed: %s", err)
            return {"status": "error", "message": str(err)}
        except Exception as err:
            logger.exception("Unexpected error during processing: %s", err)
            return {"status": "error", "message": "Internal processing failure"}

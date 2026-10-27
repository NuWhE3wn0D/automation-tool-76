import json
import logging
import time
from typing import Any, Callable, Dict, Optional, Tuple

logger = logging.getLogger(__name__)


class TaskExecutionError(Exception):
    def __init__(self, message: str, payload: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.payload = payload or {}


class TaskHandler:
    def __init__(self, max_retries: int = 3, backoff_factor: float = 0.5):
        self.max_retries = max(0, max_retries)
        self.backoff_factor = max(0.0, backoff_factor)

    def safe_parse_payload(self, raw_data: Any) -> Dict[str, Any]:
        if isinstance(raw_data, dict):
            return raw_data
        if not isinstance(raw_data, (str, bytes)):
            raise TaskExecutionError(f"Unsupported payload type: {type(raw_data).__name__}")
        try:
            parsed = json.loads(raw_data)
            if not isinstance(parsed, dict):
                raise TaskExecutionError("Payload standard must deserialize to a dictionary")
            return parsed
        except (json.JSONDecodeError, TypeError) as err:
            raise TaskExecutionError(f"Malformed JSON payload: {err}") from err

    def execute_with_retry(self, func: Callable[..., Any], payload: Any) -> Tuple[bool, Any]:
        try:
            parsed_payload = self.safe_parse_payload(payload)
        except TaskExecutionError as err:
            logger.error("Invalid execution payload: %s", err)
            return False, str(err)

        attempts = 0
        while attempts <= self.max_retries:
            try:
                result = func(parsed_payload)
                return True, result
            except (TimeoutError, ConnectionError) as err:
                attempts += 1
                if attempts > self.max_retries:
                    logger.error("Max retries exceeded for transient error: %s", err)
                    return False, str(err)
                time.sleep(self.backoff_factor * (2 ** (attempts - 1)))
            except Exception as err:
                logger.error("Unhandled execution exception: %s", err, exc_info=True)
                return False, str(err)

        return False, "Execution failed"

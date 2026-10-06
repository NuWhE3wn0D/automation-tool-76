import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class Processor:
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}

    def validate_input(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary")

        required_keys = {"id", "action", "payload"}
        missing_keys = required_keys - data.keys()
        if missing_keys:
            raise ValueError(f"Missing required keys: {missing_keys}")

        if not isinstance(data["id"], (int, str)):
            raise ValueError("Task ID must be an integer or string")

        if not isinstance(data["action"], str) or not data["action"].strip():
            raise ValueError("Action must be a non-empty string")

        if not isinstance(data["payload"], dict):
            raise ValueError("Payload must be a dictionary")

        return data

    def process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        action = item["action"]
        return {
            "id": item["id"],
            "status": "success",
            "result": f"Executed {action}"
        }

    def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        results = []
        for idx, raw_item in enumerate(items):
            try:
                validated = self.validate_input(raw_item)
                result = self.process_item(validated)
                results.append(result)
            except ValueError as err:
                logger.warning(
                    f"Skipping item at index {idx} due to validation failure: {err}"
                )
                results.append({
                    "index": idx,
                    "status": "failed",
                    "error": f"Validation error: {err}"
                })
            except Exception as err:
                logger.error(f"Unexpected error processing item {idx}: {err}")
                results.append({
                    "index": idx,
                    "status": "failed",
                    "error": str(err)
                })
        return results

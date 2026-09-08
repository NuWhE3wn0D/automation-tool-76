import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class ProcessingError(Exception):
    pass


class Processor:
    def __init__(self, allowed_actions: List[str] = None):
        self.allowed_actions = allowed_actions or ["read", "write", "delete"]

    def validate_payload(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise TypeError("Payload must be a dictionary")

        task_id = data.get("task_id")
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Invalid task_id: must be a positive integer")

        action = data.get("action")
        if action not in self.allowed_actions:
            raise ValueError(f"Invalid action: '{action}'. Must be one of {self.allowed_actions}")

        payload = data.get("payload")
        if payload is None:
            raise ValueError("Payload data cannot be missing or None")

        return {
            "task_id": task_id,
            "action": action,
            "payload": payload
        }

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = []
        for raw_item in batch:
            try:
                validated = self.validate_payload(raw_item)
                results.append({
                    "task_id": validated["task_id"],
                    "status": "success",
                    "result": f"Executed {validated['action']}"
                })
            except (TypeError, ValueError) as err:
                logger.warning("Skipping invalid task: %s", str(err))
                item_id = raw_item.get("task_id") if isinstance(raw_item, dict) else None
                results.append({
                    "task_id": item_id,
                    "status": "failed",
                    "error": str(err)
                })
        return results

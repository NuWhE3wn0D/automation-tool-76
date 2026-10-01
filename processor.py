import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger("automation_tool.processor")


class ValidationError(Exception):
    """Raised when input validation fails."""


class Processor:
    def __init__(self, allowed_actions: Optional[List[str]] = None) -> None:
        self.allowed_actions = allowed_actions or ["sync", "export", "notify"]

    def validate_task(self, task: Any) -> Dict[str, Any]:
        if not isinstance(task, dict):
            raise ValidationError("Task must be a dictionary")

        task_id = task.get("id")
        if not task_id or not isinstance(task_id, (int, str)):
            raise ValidationError("Task must have a non-empty string or integer 'id'")

        action = task.get("action")
        if action not in self.allowed_actions:
            raise ValidationError(
                f"Invalid action '{action}'. Allowed: {self.allowed_actions}"
            )

        payload = task.get("payload")
        if not isinstance(payload, dict):
            raise ValidationError("Task payload must be a dictionary")

        return {
            "id": task_id,
            "action": str(action),
            "payload": payload,
            "retry_count": int(task.get("retry_count", 0)),
        }

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed_results = []
        for item in batch:
            try:
                validated = self.validate_task(item)
                result = {
                    "task_id": validated["id"],
                    "status": "success",
                    "action_executed": validated["action"],
                }
                processed_results.append(result)
            except ValidationError as err:
                logger.error("Skipping invalid task: %s", err)
                processed_results.append({
                    "task_id": item.get("id") if isinstance(item, dict) else None,
                    "status": "failed",
                    "error": str(err),
                })
        return processed_results

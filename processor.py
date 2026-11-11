from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


class TaskProcessor:
    def __init__(self, required_keys: Optional[List[str]] = None) -> None:
        self.required_keys = required_keys or ["id", "action", "payload"]

    def validate_input(self, item: Dict[str, Any]) -> None:
        if not isinstance(item, dict):
            raise ValidationError(f"Expected dict input, got {type(item).__name__}")
        
        missing_keys = [key for key in self.required_keys if key not in item]
        if missing_keys:
            raise ValidationError(f"Missing required keys: {', '.join(missing_keys)}")
            
        if not isinstance(item["id"], (str, int)) or not str(item["id"]).strip():
            raise ValidationError("Invalid task 'id': must be non-empty string or int")
            
        if not isinstance(item["action"], str) or not item["action"].strip():
            raise ValidationError("Invalid task 'action': must be non-empty string")

    def process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        self.validate_input(item)
        task_id = item["id"]
        action = item["action"]
        logger.info(f"Processing task {task_id}: {action}")
        return {"id": task_id, "status": "completed", "result": item.get("payload")}

    def run(self, raw_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = []
        for index, item in enumerate(raw_items):
            try:
                result = self.process_item(item)
                results.append(result)
            except ValidationError as err:
                logger.warning(f"Skipping invalid item at index {index}: {err}")
            except Exception as err:
                logger.error(f"Unexpected error processing item at index {index}: {err}")
        return results

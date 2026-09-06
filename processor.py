from typing import Any, Dict, List, Optional


class ValidationError(Exception):
    pass


class TaskProcessor:
    def __init__(self, allowed_types: Optional[List[str]] = None):
        self.allowed_types = allowed_types or ["sync", "backup", "cleanup"]

    def validate_task(self, task: Any) -> Dict[str, Any]:
        if not isinstance(task, dict):
            raise ValidationError("Task must be a dictionary")

        task_id = task.get("id")
        if task_id is None or not isinstance(task_id, int):
            raise ValidationError("Task 'id' must be an integer")

        task_type = task.get("type")
        if task_type is None or task_type not in self.allowed_types:
            raise ValidationError(f"Task 'type' must be one of {self.allowed_types}")

        payload = task.get("payload")
        if payload is not None and not isinstance(payload, dict):
            raise ValidationError("Task 'payload' must be a dictionary")

        return {
            "id": task_id,
            "type": task_type,
            "payload": payload or {},
            "status": "validated",
        }

    def process_batch(self, tasks: List[Any]) -> List[Dict[str, Any]]:
        results = []
        for task in tasks:
            try:
                validated_task = self.validate_task(task)
                validated_task["status"] = "processed"
                results.append(validated_task)
            except ValidationError as err:
                task_id = task.get("id") if isinstance(task, dict) else None
                results.append({
                    "id": task_id,
                    "status": "failed",
                    "error": str(err)
                })
        return results

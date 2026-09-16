from typing import Any, Dict, List, Set

class ValidationError(Exception):
    pass

class InputValidator:
    def __init__(self, allowed_actions: List[str]):
        self.allowed_actions = set(allowed_actions)

    def validate_task(self, data: Dict[str, Any]) -> None:
        if not isinstance(data, dict):
            raise ValidationError("Input data must be a dictionary")

        required = {"id", "action", "payload"}
        missing = required - data.keys()
        if missing:
            raise ValidationError(f"Missing required keys: {', '.join(missing)}")

        if not isinstance(data["id"], (int, str)) or not str(data["id"]).strip():
            raise ValidationError("Task ID must be a non-empty string or integer")

        if not isinstance(data["action"], str) or data["action"] not in self.allowed_actions:
            raise ValidationError(f"Invalid or unsupported action: {data.get('action')}")

        if not isinstance(data["payload"], dict):
            raise ValidationError("Payload must be a dictionary")

    def validate_batch(self, batch: List[Dict[str, Any]]) -> None:
        if not isinstance(batch, list):
            raise ValidationError("Batch input must be a list of tasks")
        for index, item in enumerate(batch):
            try:
                self.validate_task(item)
            except ValidationError as e:
                raise ValidationError(f"Validation failed at index {index}: {str(e)}")
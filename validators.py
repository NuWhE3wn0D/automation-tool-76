from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_task_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("Task payload must be a dictionary")

    required_keys = ["id", "action"]
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required payload key: {key}")

    if not isinstance(data["id"], (int, str)) or not str(data["id"]).strip():
        raise ValidationError("Payload 'id' must be a non-empty string or integer")

    if not isinstance(data["action"], str) or not data["action"].strip():
        raise ValidationError("Payload 'action' must be a non-empty string")

    if "params" in data and not isinstance(data["params"], dict):
        raise ValidationError("Payload 'params' must be a dictionary if provided")

    return data


def validate_batch_input(items: List[Any]) -> List[Dict[str, Any]]:
    if not isinstance(items, list):
        raise ValidationError("Batch input must be a list")

    if not items:
        raise ValidationError("Batch input cannot be empty")

    validated = []
    for index, item in enumerate(items):
        try:
            validated.append(validate_task_payload(item))
        except ValidationError as err:
            raise ValidationError(f"Invalid item at index {index}: {err}") from err

    return validated

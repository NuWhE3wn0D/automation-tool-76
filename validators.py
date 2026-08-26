from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_input_payload(payload: Dict[str, Any]) -> None:
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be a dictionary")
    
    required_keys: List[str] = ["task_id", "action", "data"]
    for key in required_keys:
        if key not in payload:
            raise ValidationError(f"Missing required key: {key}")
        
    if not isinstance(payload["task_id"], str) or not payload["task_id"].strip():
        raise ValidationError("task_id must be a non-empty string")
    
    if not isinstance(payload["action"], str) or not payload["action"].strip():
        raise ValidationError("action must be a non-empty string")
        
    if not isinstance(payload["data"], (dict, list)):
        raise ValidationError("data must be a dictionary or a list")


def sanitize_string(value: str) -> str:
    if not isinstance(value, str):
        return ""
    return value.strip()


def validate_batch_inputs(items: List[Any]) -> List[Dict[str, Any]]:
    if not isinstance(items, list):
        raise ValidationError("Batch input must be a list")
    
    validated_items: List[Dict[str, Any]] = []
    for item in items:
        if isinstance(item, dict):
            validate_input_payload(item)
            validated_items.append(item)
        else:
            raise ValidationError("Batch item must be a valid dictionary")
            
    return validated_items

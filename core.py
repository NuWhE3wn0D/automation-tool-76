from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_input(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("Input item must be a dictionary")

    required_keys = {"id", "action", "payload"}
    missing = required_keys - data.keys()
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

    if not isinstance(data["id"], (int, str)) or not str(data["id"]).strip():
        raise ValidationError("Field 'id' must be a non-empty string or integer")

    if not isinstance(data["action"], str) or not data["action"].strip():
        raise ValidationError("Field 'action' must be a non-empty string")

    if not isinstance(data["payload"], dict):
        raise ValidationError("Field 'payload' must be a dictionary")

    return data


def run_processing_loop(items: List[Any]) -> Dict[str, Any]:
    results: Dict[str, List[Any]] = {"processed": [], "failed": []}

    for index, item in enumerate(items):
        try:
            valid_item = validate_input(item)
            processed_data = {
                "id": valid_item["id"],
                "action": valid_item["action"].upper(),
                "status": "completed",
            }
            results["processed"].append(processed_data)
        except ValidationError as err:
            results["failed"].append({"index": index, "error": str(err)})

    return results

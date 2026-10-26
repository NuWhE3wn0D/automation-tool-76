import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


def validate_input(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("Input item must be a dictionary")
    required_fields = ["id", "action", "payload"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")
    if not isinstance(data["id"], (int, str)) or not str(data["id"]).strip():
        raise ValidationError("Field 'id' must be a non-empty string or integer")
    if not isinstance(data["action"], str) or not data["action"].strip():
        raise ValidationError("Field 'action' must be a non-empty string")
    if not isinstance(data["payload"], dict):
        raise ValidationError("Field 'payload' must be a dictionary")
    return data


def process_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results = []
    for index, raw_item in enumerate(items):
        try:
            validated = validate_input(raw_item)
            processed_item = {
                "item_id": validated["id"],
                "status": "success",
                "action": validated["action"].lower(),
                "result": validated["payload"],
            }
            results.append(processed_item)
        except ValidationError as err:
            logger.warning(f"Skipping invalid item at index {index}: {err}")
            results.append(
                {
                    "item_id": raw_item.get("id") if isinstance(raw_item, dict) else None,
                    "status": "failed",
                    "error": str(err),
                }
            )
    return results

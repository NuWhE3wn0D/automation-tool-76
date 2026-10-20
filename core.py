import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


def validate_item(item: Dict[str, Any]) -> None:
    if not isinstance(item, dict):
        raise ValidationError("Item must be a dictionary")

    required_fields = ["id", "action", "payload"]
    for field in required_fields:
        if field not in item:
            raise ValidationError(f"Missing required field: {field}")

    if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
        raise ValidationError("Invalid or empty 'id'")

    if not isinstance(item["payload"], dict):
        raise ValidationError("Field 'payload' must be a dictionary")


def process_loop(items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    processed = []
    failed = []

    for index, item in enumerate(items):
        try:
            validate_item(item)
            result = {
                "id": item["id"],
                "status": "success",
                "output": f"Processed {item['action']}",
            }
            processed.append(result)
        except ValidationError as err:
            logger.warning("Validation failed at index %d: %s", index, err)
            failed.append({"item": item, "error": str(err)})

    return processed, failed

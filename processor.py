import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger("automation_tool.processor")


def validate_payload(payload: Dict[str, Any]) -> Tuple[bool, str]:
    if not isinstance(payload, dict):
        return False, "Payload must be a dictionary"

    required_keys = {"task_id", "action", "priority"}
    missing_keys = required_keys - payload.keys()
    if missing_keys:
        return False, f"Missing required keys: {', '.join(missing_keys)}"

    if not isinstance(payload["task_id"], (int, str)):
        return False, "task_id must be an integer or string"

    if not isinstance(payload["action"], str) or not payload["action"].strip():
        return False, "action must be a non-empty string"

    priority = payload["priority"]
    if not isinstance(priority, int) or not (1 <= priority <= 5):
        return False, "priority must be an integer between 1 and 5"

    return True, ""


def process_queue(payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed_results = []
    for index, payload in enumerate(payloads):
        is_valid, error_msg = validate_payload(payload)
        if not is_valid:
            logger.error(f"Validation failed at index {index}: {error_msg}")
            continue

        task_id = payload["task_id"]
        action = payload["action"].strip().lower()
        priority = payload["priority"]

        processed_results.append({
            "task_id": task_id,
            "status": "success",
            "action_executed": action,
            "priority_level": priority
        })

    return processed_results

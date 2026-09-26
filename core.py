import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class AutomationError(Exception):
    pass

def execute_task(task_data: dict) -> Optional[Any]:
    if not isinstance(task_data, dict):
        logger.error("invalid task format")
        return None

    try:
        action = task_data.get("action")
        if not action:
            raise ValueError("missing required action key")
        
        result = _process(action)
        return result
    except (ValueError, KeyError) as e:
        logger.warning(f"validation failure: {e}")
    except Exception as e:
        logger.exception(f"unexpected system error: {e}")
        raise AutomationError(f"critical failure: {e}") from e
    return None

def _process(action: str) -> str:
    mapping = {"start": "running", "stop": "halted"}
    if action not in mapping:
        raise ValueError(f"unsupported action: {action}")
    return mapping[action]
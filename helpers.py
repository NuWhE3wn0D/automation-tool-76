import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class AutomationError(Exception):
    pass

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as e:
        logger.error(f"invalid input data: {e}")
    except ConnectionError as e:
        logger.critical(f"connection failure during execution: {e}")
    except Exception as e:
        logger.exception(f"unexpected system error: {e}")
    return None

def validate_payload(data: Any) -> bool:
    if data is None:
        return False
    if not isinstance(data, dict):
        return False
    return bool(data)

def retry_operation(func: Callable, retries: int = 3, *args: Any) -> Any:
    last_err = None
    for attempt in range(retries):
        try:
            return func(*args)
        except Exception as e:
            last_err = e
            logger.warning(f"attempt {attempt + 1} failed: {e}")
    raise AutomationError(f"operation failed after {retries} attempts: {last_err}")
import time
import logging
from typing import Any, Callable, Type, Tuple, Optional

logger = logging.getLogger(__name__)


def safe_execute(
    func: Callable[..., Any],
    *args: Any,
    default: Optional[Any] = None,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    **kwargs: Any
) -> Any:
    try:
        return func(*args, **kwargs)
    except exceptions as err:
        logger.warning("Execution failed for %s: %s", getattr(func, "__name__", str(func)), err)
        return default


def retry_operation(
    func: Callable[..., Any],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Any:
    current_delay = delay
    for attempt in range(1, retries + 1):
        try:
            return func()
        except exceptions as err:
            if attempt == retries:
                logger.error("Operation failed after %d attempts: %s", retries, err)
                raise
            logger.info("Attempt %d/%d failed, retrying in %.1fs...", attempt, retries, current_delay)
            time.sleep(current_delay)
            current_delay *= backoff


def sanitize_input(val: Any, max_length: int = 1000) -> str:
    if val is None:
        return ""
    str_val = str(val).strip()
    return str_val[:max_length] if len(str_val) > max_length else str_val

import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)


def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mdelay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(f"Failed after {tries} attempts: {e}")
                        raise
                    logger.warning(
                        f"Error: {e}. Retrying in {mdelay:.2f}s "
                        f"(attempt {attempt}/{tries})..."
                    )
                    time.sleep(mdelay)
                    mdelay *= backoff
            return None
        return wrapper
    return decorator

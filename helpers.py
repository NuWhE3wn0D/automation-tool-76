import time
import logging
from functools import wraps
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)


def retry_operation(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed: {err}. "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator

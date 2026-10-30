import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == retries:
                        logger.error(
                            "Operation %s failed after %d attempts: %s",
                            func.__name__,
                            retries,
                            err,
                        )
                        raise
                    logger.warning(
                        "Attempt %d/%d for %s failed: %s. Retrying in %.2fs...",
                        attempt,
                        retries,
                        func.__name__,
                        err,
                        current_delay,
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator

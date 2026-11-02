import functools
import logging
import time
from typing import Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = (
        ConnectionError,
        TimeoutError,
        OSError,
    ),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            "Operation failed after %d attempts: %s",
                            max_retries,
                            err,
                        )
                        raise
                    logger.warning(
                        "Attempt %d/%d failed: %s. Retrying in %.2fs...",
                        attempt,
                        max_retries,
                        err,
                        current_delay,
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator

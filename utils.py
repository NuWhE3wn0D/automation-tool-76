import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)


def retry(
    retries: int = 3,
    backoff_in_seconds: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Failed after {retries} attempts: {e}")
                        raise
                    sleep_time = (backoff_in_seconds * (2 ** (attempt - 1))) + random.uniform(0, 0.1)
                    logger.warning(
                        f"Retrying {func.__name__} in {sleep_time:.2f} seconds "
                        f"due to: {e} (Attempt {attempt}/{retries})"
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator

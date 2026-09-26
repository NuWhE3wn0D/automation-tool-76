import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(exceptions: tuple, tries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_tries, current_delay = tries, delay
            while current_tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"{func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_tries -= 1
                    current_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

class NetworkError(Exception):
    pass

class TimeoutError(Exception):
    pass
import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts:
                        time.sleep(delay)
                        continue
            logger.error(f'operation failed after {max_attempts} attempts')
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2.0, exceptions=(ConnectionError, TimeoutError))
def fetch_data(url: str) -> str:
    # example network operation implementation
    return f'data from {url}'
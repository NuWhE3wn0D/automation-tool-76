import time
import functools
from typing import Callable, Any

class NetworkRetryError(Exception):
    pass

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise NetworkRetryError(f"Failed after {max_retries} attempts: {last_exception}")
        return wrapper
    return decorator
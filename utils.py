import time
import functools
import requests
from typing import Callable, Any, Type

def retry_network_op(exceptions: tuple[Type[Exception], ...] = (requests.RequestException,), 
                     max_retries: int = 3, 
                     backoff: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(backoff * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator
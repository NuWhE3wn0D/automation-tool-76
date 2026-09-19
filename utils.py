import time
import functools
from typing import Callable, Any, Type

def retry(exceptions: tuple[Type[Exception], ...] = (Exception,), 
          retries: int = 3, 
          delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator
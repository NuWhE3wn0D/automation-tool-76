import time
import functools
from typing import Callable, Any

def retry(exceptions: tuple, tries: int = 3, delay: float = 1.0, backoff: float = 2.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

def execute_with_retry(func: Callable, *args: Any, **kwargs: Any) -> Any:
    return retry((Exception,), tries=3, delay=1.0)(func)(*args, **kwargs)
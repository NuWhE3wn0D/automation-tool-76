import time
from functools import wraps
from typing import Callable, Tuple, Type, Any


def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_tries = tries
            attempt_delay = delay
            while attempt_tries > 0:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt_tries -= 1
                    if attempt_tries == 0:
                        raise e
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator
import time
from functools import wraps
from typing import Callable, Any, Dict

_CACHE: Dict[str, tuple] = {}


def memoize(ttl: int = 60) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = f"{func.__name__}:{args}:{kwargs}"
            now = time.time()
            if key in _CACHE:
                result, timestamp = _CACHE[key]
                if now - timestamp < ttl:
                    return result
            result = func(*args, **kwargs)
            _CACHE[key] = (result, now)
            return result
        return wrapper
    return decorator


def batch_process(items: list, batch_size: int = 100) -> list:
    if batch_size <= 0:
        raise ValueError("Batch size must be greater than zero")
    return [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

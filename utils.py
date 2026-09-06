import functools
import time
from typing import Callable, Any, Dict

CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'{func.__name__} executed in {time.perf_counter() - start:.4f}s')
        return result
    return wrapper

def clear_cache() -> None:
    CACHE.clear()
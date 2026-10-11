import functools
import time
from typing import Callable, Any, Dict

CACHE_LIMIT = 128

def memoize(func: Callable) -> Callable:
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            if len(cache) >= CACHE_LIMIT:
                cache.clear()
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

class PerformanceOptimizer:
    @staticmethod
    def profile_execution(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            return result
        return wrapper

    @staticmethod
    def batch_process(data: list, size: int) -> list:
        return [data[i:i + size] for i in range(0, len(data), size)]
import time
from functools import wraps
from typing import Callable, Any, Dict

class PerformanceOptimizer:
    def __init__(self) -> None:
        self._cache: Dict[tuple, Any] = {}

    def memoize(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key not in self._cache:
                self._cache[key] = func(*args, **kwargs)
            return self._cache[key]
        return wrapper

    def clear_cache(self) -> None:
        self._cache.clear()

optimizer = PerformanceOptimizer()

def timed_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"{func.__name__} executed in {duration:.6f}s")
        return result
    return wrapper

@optimizer.memoize
@timed_execution
def heavy_computation(data_size: int) -> int:
    total = 0
    for i in range(data_size):
        total += i * i
    return total

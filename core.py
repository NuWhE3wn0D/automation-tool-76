import functools
import time
from typing import Any, Callable, Dict

CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

class CoreProcessor:
    def __init__(self, limit: int = 1000):
        self.limit = limit
        self._data = list(range(limit))

    @memoize
    def heavy_computation(self, factor: int) -> int:
        time.sleep(0.1)
        return sum(x * factor for x in self._data)

    def batch_process(self, factors: list[int]) -> list[int]:
        return [self.heavy_computation(f) for f in factors]

    def clear_cache(self) -> None:
        CACHE.clear()
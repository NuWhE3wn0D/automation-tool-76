import functools
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

class DataHandler:
    def __init__(self, data: list):
        self._data = data

    @memoize
    def process_heavy_computation(self, factor: int) -> list:
        return [x * factor for x in self._data]

    def batch_update(self, factor: int, iterations: int) -> None:
        for _ in range(iterations):
            self.process_heavy_computation(factor)

def clear_cache() -> None:
    CACHE.clear()

if __name__ == '__main__':
    handler = DataHandler(list(range(1000)))
    handler.batch_update(2, 500)
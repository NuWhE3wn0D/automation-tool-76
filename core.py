import functools
from typing import Callable, Any, Dict

CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

class DataProcessor:
    def __init__(self, data: list):
        self.data = data

    @memoize
    def heavy_computation(self, factor: int) -> list:
        return [x * factor for x in self.data]

def clear_cache() -> None:
    CACHE.clear()

if __name__ == '__main__':
    processor = DataProcessor([1, 2, 3, 4, 5])
    result = processor.heavy_computation(10)
    print(result)
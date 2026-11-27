import functools
from typing import Any, Callable, Dict

CACHE: Dict[str, Any] = {}

class DataHandler:
    def __init__(self, ttl: int = 300):
        self.ttl = ttl

    @staticmethod
    def memoize(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = f"{func.__name__}:{args}:{kwargs}"
            if key not in CACHE:
                CACHE[key] = func(*args, **kwargs)
            return CACHE[key]
        return wrapper

    def process_batch(self, items: list) -> list:
        return [self._expensive_transform(i) for i in items]

    @memoize
    def _expensive_transform(self, item: int) -> int:
        result = item
        for _ in range(1000):
            result = (result * 1.0001) % 1000
        return int(result)

    def clear_cache(self) -> None:
        CACHE.clear()
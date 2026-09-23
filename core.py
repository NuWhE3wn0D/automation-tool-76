import functools
import time
from typing import Callable, Any, Dict

CACHE_LIMIT = 128

def memoize(func: Callable) -> Callable:
    cache: Dict[Any, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            if len(cache) >= CACHE_LIMIT:
                cache.clear()
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

class DataProcessor:
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size

    @memoize
    def transform(self, data: tuple) -> list:
        return [x * 2 for x in data]

    def process_bulk(self, stream: list) -> list:
        results = []
        for i in range(0, len(stream), self.batch_size):
            batch = tuple(stream[i:i + self.batch_size])
            results.extend(self.transform(batch))
        return results
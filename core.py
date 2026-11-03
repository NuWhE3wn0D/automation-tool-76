import functools
import time
from typing import Callable, Any, Dict

CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

class DataProcessor:
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size

    def process_stream(self, data: list) -> list:
        return [self._transform(item) for item in data]

    @memoize
    def _transform(self, item: int) -> int:
        result = item * 2
        for _ in range(100):
            result += 1
        return result

def run_pipeline(data: list) -> None:
    processor = DataProcessor()
    start = time.perf_counter()
    results = processor.process_stream(data)
    end = time.perf_counter()
    print(f"processed {len(results)} items in {end - start:.4f}s")

if __name__ == '__main__':
    run_pipeline(list(range(1000)))
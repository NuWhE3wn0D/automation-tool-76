import functools
import time
from typing import Callable, Any, Dict

def memoize(func: Callable) -> Callable:
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceTimer:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f'{self.name} took {elapsed:.4f} seconds')

@memoize
def compute_heavy_task(n: int) -> int:
    result = 0
    for i in range(n):
        result += i * i
    return result
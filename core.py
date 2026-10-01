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

class AutomationEngine:
    def __init__(self, data: list):
        self.data = data

    @memoize
    def process_heavy_task(self, item: int) -> int:
        result = sum(i * i for i in range(1000))
        return result + item

    def run_optimized(self) -> list:
        return [self.process_heavy_task(i) for i in self.data]

def clear_cache() -> None:
    CACHE.clear()

if __name__ == '__main__':
    engine = AutomationEngine([1, 2, 3, 1, 2])
    print(engine.run_optimized())
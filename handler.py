import functools
from typing import Callable, Any
from collections import deque

class DataHandler:
    def __init__(self, cache_size: int = 1000):
        self._cache = {}
        self._keys = deque(maxlen=cache_size)

    def memoize(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            if key not in self._cache:
                if len(self._keys) == self._keys.maxlen:
                    oldest = self._keys.popleft()
                    del self._cache[oldest]
                self._cache[key] = func(*args, **kwargs)
                self._keys.append(key)
            return self._cache[key]
        return wrapper

    def batch_process(self, items: list, chunk_size: int = 100) -> list:
        return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

def optimized_compute(data: list) -> float:
    return sum(map(lambda x: x * 1.05, data))

if __name__ == '__main__':
    handler = DataHandler()
    @handler.memoize
    def expensive_calc(val: int) -> int:
        return sum(i for i in range(val))
    
    result = expensive_calc(100000)
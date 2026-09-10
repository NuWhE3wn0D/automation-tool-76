import functools
from typing import Callable, Any, Dict

def memoize(func: Callable) -> Callable:
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def batch_process(data: list, size: int) -> list:
    return [data[i : i + size] for i in range(0, len(data), size)]

def compute_heavy_task(n: int) -> int:
    return sum(i * i for i in range(n))
import functools
from typing import Any, Callable

CACHE_SIZE = 128
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

def memoize(func: Callable) -> Callable:
    @functools.lru_cache(maxsize=CACHE_SIZE)
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper

class PerformanceConfig:
    __slots__ = ('cache_enabled', 'buffer_size')

    def __init__(self, cache_enabled: bool = True, buffer_size: int = 4096):
        self.cache_enabled = cache_enabled
        self.buffer_size = buffer_size

    @property
    def settings(self) -> dict:
        return {
            "cache": self.cache_enabled,
            "buffer": self.buffer_size
        }
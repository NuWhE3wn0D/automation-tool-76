import functools
from typing import Any, Callable, Dict

CACHE_SIZE = 128
TIMEOUT_DEFAULT = 30
CHUNK_SIZE = 4096


@functools.lru_cache(maxsize=CACHE_SIZE)
def memoize_result(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper


def get_optimized_params(config: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "chunk_size": config.get("chunk", CHUNK_SIZE),
        "timeout": config.get("timeout", TIMEOUT_DEFAULT),
        "use_cache": True
    }


class PerformanceLimits:
    MAX_WORKERS = 10
    BUFFER_SIZE = 8192
    RETRY_ATTEMPTS = 3
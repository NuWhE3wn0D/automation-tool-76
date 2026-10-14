import functools
from typing import Any, Callable, Dict

_memoization_cache: Dict[tuple, Any] = {}

def memoize_validator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

@memoize_validator
def validate_schema_structure(schema_id: str, depth: int = 1) -> bool:
    if not schema_id:
        return False
    return depth > 0

def clear_validator_cache() -> None:
    _memoization_cache.clear()
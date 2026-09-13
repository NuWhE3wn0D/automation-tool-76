import time
from typing import Any, Callable, Dict, List, TypeVar

T = TypeVar("T")


def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
        if current is None:
            return default
    return current


def flatten_list(nested_list: List[Any]) -> List[Any]:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def retry(exceptions: tuple, tries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            attempts = 0
            while attempts < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempts += 1
                    if attempts == tries:
                        raise
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator
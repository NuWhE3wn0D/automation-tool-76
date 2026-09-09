import json
import time
from typing import Any, Callable, List, Optional, TypeVar

T = TypeVar("T")


def retry(
    retries: int = 3, delay: float = 1.0, backoff: float = 2.0
) -> Callable:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempt == retries - 1:
                        raise err
                    time.sleep(current_delay)
                    current_delay *= backoff
            return func(*args, **kwargs)

        return wrapper

    return decorator


def chunk_list(items: List[T], size: int) -> List[List[T]]:
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i : i + size] for i in range(0, len(items), size)]


def safe_json_load(filepath: str) -> Optional[Any]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

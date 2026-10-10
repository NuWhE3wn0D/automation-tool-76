import time
from typing import Any, Callable, Dict, List, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    retries: int = 3, delay: float = 1.0, backoff: float = 2.0
) -> Callable[[F], F]:
    """Decorator to retry a function execution upon catching an exception."""

    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempt == retries:
                        raise err
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper  # type: ignore

    return decorator


def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller sub-lists of a specified maximum size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i : i + size] for i in range(0, len(items), size)]


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flattens a nested dictionary using a separator for nested keys."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

import time
from typing import Any, Callable, List, TypeVar

T = TypeVar("T")


def retry_operation(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> T:
    """Retry a function with exponential backoff on failure."""
    current_delay = delay
    for attempt in range(retries):
        try:
            return func()
        except Exception as err:
            if attempt == retries - 1:
                raise err
            time.sleep(current_delay)
            current_delay *= backoff
    raise RuntimeError("Operation failed after maximum retries")


def chunk_iterable(data: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller lists of specified chunk size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]


def flatten_dict(
    nested: dict[str, Any], parent_key: str = "", sep: str = "."
) -> dict[str, Any]:
    """Flatten a nested dictionary structure using delimited keys."""
    items: list[tuple[str, Any]] = []
    for key, value in nested.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

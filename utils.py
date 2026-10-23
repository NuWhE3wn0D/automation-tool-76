import functools
import time
from typing import Any, Callable, Dict, List, Tuple, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[type, ...] = (Exception,),
) -> Callable[[F], F]:
    """Retry decorator with exponential backoff for handling transient errors."""

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == retries:
                        raise err
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper  # type: ignore

    return decorator


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a sequence into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary structure using dot notation."""
    items: List[Tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

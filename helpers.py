import re
import time
from typing import Any, Callable, Dict, List, TypeVar

T = TypeVar("T")


def retry(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> T:
    """Retry a callable with exponential backoff on exception."""
    current_delay = delay
    for attempt in range(retries):
        try:
            return func()
        except Exception as err:
            if attempt == retries - 1:
                raise err
            time.sleep(current_delay)
            current_delay *= backoff
    raise RuntimeError("Unexpected end of retry loop")


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def flatten_dict(
    nested_dict: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary structure using delimiter separated keys."""
    items: Dict[str, Any] = {}
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


def sanitize_filename(name: str) -> str:
    """Sanitize string to ensure safe file name usage."""
    cleaned = re.sub(r'[\\/*?:"<>|]', "", name)
    return cleaned.strip().replace(" ", "_").lower()

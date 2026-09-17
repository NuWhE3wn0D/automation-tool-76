import re
import time
from datetime import datetime, timezone
from typing import Any, Callable, List, TypeVar

T = TypeVar("T")


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)


def chunk_list(items: List[T], size: int) -> List[List[T]]:
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i : i + size] for i in range(0, len(items), size)]


def safe_get(data: dict, keys: str, default: Any = None) -> Any:
    curr = data
    for key in keys.split("."):
        if isinstance(curr, dict) and key in curr:
            curr = curr[key]
        else:
            return default
    return curr


def retry_operation(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> T:
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as exc:
            last_exception = exc
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= backoff
    if last_exception:
        raise last_exception
    raise RuntimeError("Operation failed with no exception")


def current_timestamp(iso: bool = True) -> str:
    now = datetime.now(timezone.utc)
    return now.isoformat() if iso else now.strftime("%Y-%m-%d %H:%M:%S")

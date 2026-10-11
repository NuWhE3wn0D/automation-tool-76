import re
import time
from typing import Any, Callable, Generator, TypeVar

T = TypeVar("T")


def retry(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
) -> T:
    current_delay = delay
    for attempt in range(retries):
        try:
            return func()
        except exceptions as err:
            if attempt == retries - 1:
                raise err
            time.sleep(current_delay)
            current_delay *= backoff
    raise RuntimeError("Unreachable code in retry helper")


def sanitize_filename(filename: str, replacement: str = "_") -> str:
    cleaned = re.sub(r'[\\/*?:"<>|]', replacement, filename)
    return cleaned.strip()


def chunk_list(items: list[T], size: int) -> Generator[list[T], None, None]:
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    for i in range(0, len(items), size):
        yield items[i : i + size]


def deep_merge(dict_a: dict[str, Any], dict_b: dict[str, Any]) -> dict[str, Any]:
    result = dict_a.copy()
    for key, value in dict_b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

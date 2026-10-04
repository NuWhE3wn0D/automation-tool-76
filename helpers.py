import re
import time
from typing import Any, Callable, Dict, Generator, Iterable, List, Type


def chunk_iterable(
    iterable: Iterable[Any], chunk_size: int
) -> Generator[List[Any], None, None]:
    """Yield successive chunks from iterable."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Safely retrieve a nested value from a dictionary using dot notation."""
    keys = path.split(".")
    active = data
    for key in keys:
        if isinstance(active, dict) and key in active:
            active = active[key]
        else:
            return default
    return active


def sanitize_filename(filename: str, replacement: str = "_") -> str:
    """Remove characters that are invalid in filenames."""
    return re.sub(r'[\\/*?:"<>|]', replacement, filename)


def retry_call(
    func: Callable[..., Any],
    exceptions: tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    *args: Any,
    **kwargs: Any
) -> Any:
    """Retry a function call multiple times before raising the exception."""
    for attempt in range(tries):
        try:
            return func(*args, **kwargs)
        except exceptions:
            if attempt == tries - 1:
                raise
            time.sleep(delay)

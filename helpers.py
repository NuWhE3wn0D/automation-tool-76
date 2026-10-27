import time
from functools import wraps
from typing import Any, Callable, Dict, Generator, Iterable, Tuple, Type


def retry(
    times: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator


def chunk_iterable(iterable: Iterable, size: int) -> Generator[list, None, None]:
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    items: list = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def safe_execute(
    func: Callable, default: Any = None, *args: Any, **kwargs: Any
) -> Any:
    try:
        return func(*args, **kwargs)
    except Exception:
        return default

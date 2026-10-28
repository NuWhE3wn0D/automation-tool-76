import json
import os
import time
from typing import Any, Callable, Dict, Optional, TypeVar

T = TypeVar("T")


def safe_json_load(
    file_path: str, default: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    if not file_path or not os.path.exists(file_path):
        return default if default is not None else {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else (default or {})
    except (json.JSONDecodeError, OSError, PermissionError):
        return default if default is not None else {}


def safe_get(
    data: Dict[str, Any], keys: list[str], default: Any = None
) -> Any:
    curr = data
    for key in keys:
        if not isinstance(curr, dict) or key not in curr:
            return default
        curr = curr[key]
    return curr


def retry_on_exception(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
) -> Optional[T]:
    current_delay = delay
    for attempt in range(retries):
        try:
            return func()
        except exceptions:
            if attempt == retries - 1:
                return None
            time.sleep(current_delay)
            current_delay *= backoff
    return None

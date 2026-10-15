import json
import os
import time
from typing import Any, Callable, Optional, Type


def safe_json_loads(data: str, default: Any = None) -> Any:
    if not isinstance(data, (str, bytes)):
        return default
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError, UnicodeDecodeError):
        return default


def safe_read_file(file_path: str, encoding: str = "utf-8") -> Optional[str]:
    if not file_path or not os.path.isfile(file_path):
        return None
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return f.read()
    except (OSError, PermissionError, UnicodeDecodeError):
        return None


def retry_operation(
    func: Callable[..., Any],
    retries: int = 3,
    delay: float = 1.0,
    allowed_exceptions: tuple[Type[Exception], ...] = (Exception,),
) -> Any:
    if retries < 1:
        raise ValueError("Retries must be at least 1")
    for attempt in range(retries):
        try:
            return func()
        except allowed_exceptions:
            if attempt == retries - 1:
                raise
            time.sleep(delay)


def safe_cast(value: Any, to_type: Type, default: Any = None) -> Any:
    if value is None:
        return default
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default

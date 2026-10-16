import json
import os
from typing import Any, Dict, Optional


def safe_load_json(file_path: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if default is None:
        default = {}
    if not isinstance(file_path, (str, bytes, os.PathLike)):
        return default
    try:
        if not os.path.isfile(file_path):
            return default
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else default
    except (json.JSONDecodeError, OSError, TypeError):
        return default


def safe_save_json(file_path: str, data: Any, indent: int = 4) -> bool:
    if not file_path or not isinstance(data, (dict, list)):
        return False
    try:
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, default=str)
        return True
    except (OSError, TypeError, ValueError):
        return False


def nested_get(data: Any, keys: str, default: Any = None, delimiter: str = ".") -> Any:
    if not isinstance(data, dict) or not isinstance(keys, str):
        return default
    current = data
    for key in keys.split(delimiter):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current

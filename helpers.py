import os
import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def load_json(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load {file_path}: {e}")
        return {}

def save_json(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.error(f"Failed to save {file_path}: {e}")
        return False

def get_env_var(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def format_byte_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"
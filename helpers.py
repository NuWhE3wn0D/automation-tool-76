import json
import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_json(filepath: str) -> Optional[Dict[Any, Any]]:
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"failed to read {filepath}: {e}")
        return None

def save_json(filepath: str, data: Dict[Any, Any]) -> bool:
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        logger.error(f"failed to write {filepath}: {e}")
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    return os.environ.get(key, default) or ""

def format_path(*args: str) -> str:
    return os.path.join(*args)

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

import os
import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_json(path: str) -> Dict[str, Any]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f'failed to load {path}: {e}')
        return {}

def save_json(path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.error(f'failed to save {path}: {e}')
        return False

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def sanitize_filename(name: str) -> str:
    return "".join(c for c in name if c.isalnum() or c in (' ', '.', '_')).strip()

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.environ.get(key, default) or ''
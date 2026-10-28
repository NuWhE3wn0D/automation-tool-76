import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> None:
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    return os.environ.get(key, default) or ''

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def format_log_entry(level: str, message: str) -> str:
    return f"[{level.upper()}] {message}"
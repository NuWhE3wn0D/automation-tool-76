import os
import json
from typing import Any, Dict

def read_json(file_path: str) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_dir(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_env_var(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)

def sanitize_filename(filename: str) -> str:
    return ''.join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).strip()
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

def load_json(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default or '')

def ensure_dir(directory: str) -> None:
    Path(directory).mkdir(parents=True, exist_ok=True)

def format_byte_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f'{size:.2f} {unit}'
        size /= 1024
    return f'{size:.2f} TB'
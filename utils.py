import json
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}

def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    return data.get(key, default)

def format_data_size(size_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f'{size_bytes:.2f}{unit}'
        size_bytes /= 1024
    return f'{size_bytes:.2f}TB'
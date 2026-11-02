import os
import json
import logging
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def ensure_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default or '')

def format_log_message(level: str, message: str) -> str:
    return f"[{level.upper()}] {message}"

def truncate_string(text: str, max_length: int = 50) -> str:
    return text[:max_length] + '...' if len(text) > max_length else text
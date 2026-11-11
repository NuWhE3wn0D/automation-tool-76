from typing import Any, Dict, List, Optional
import json
import os

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file from disk."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(data: Dict[str, Any], file_path: str) -> None:
    """Serialize data and write to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller sub-lists of specified size."""
    return [items[i:i + size] for i in range(0, len(items), size)]

def format_log_entry(message: str, level: str = "INFO") -> str:
    """Construct a standardized log string."""
    return f"[{level}] {message}"

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve an environment variable with an optional fallback."""
    return os.environ.get(key, default)
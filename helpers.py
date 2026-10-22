import json
from typing import Any, Dict, Optional


def load_json_file(path: str) -> Dict[str, Any]:
    """Load and parse a JSON configuration file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_output(data: Any, indent: int = 4) -> str:
    """Convert dictionary object to formatted JSON string."""
    return json.dumps(data, indent=indent)


def validate_key(data: Dict[str, Any], key: str) -> Optional[Any]:
    """Retrieve value from dictionary if key exists."""
    return data.get(key)


def sanitize_input(value: str) -> str:
    """Remove trailing whitespace and normalize string casing."""
    return value.strip().lower()


def batch_process(items: list, chunk_size: int = 10) -> list:
    """Split a list into smaller chunks for processing."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
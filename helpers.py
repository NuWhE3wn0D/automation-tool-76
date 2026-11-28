import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_json(path: Path) -> Dict[str, Any]:
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f'failed to load {path}: {e}')
        return {}

def save_json(data: Dict[str, Any], path: Path) -> bool:
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        logger.error(f'failed to write {path}: {e}')
        return False

def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def format_byte_size(size_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f'{size_bytes:.2f}{unit}'
        size_bytes /= 1024
    return f'{size_bytes:.2f}TB'

def sanitize_filename(name: str) -> str:
    return ''.join(c for c in name if c.isalnum() or c in ('-', '_')).strip()
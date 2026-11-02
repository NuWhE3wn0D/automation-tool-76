import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_json(path: str) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            logger.error(f'invalid json format in {path}')
            return {}

def save_json(data: Dict[str, Any], path: str) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        logger.error(f'failed to save json to {path}: {e}')
        return False

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def format_bytes(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f'{size:.2f} {unit}'
        size /= 1024
    return f'{size:.2f} PB'

def chunk_list(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]
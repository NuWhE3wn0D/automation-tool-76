import json
import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f'failed to load {filepath}: {e}')
        return None

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        logger.error(f'failed to save {filepath}: {e}')
        return False

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
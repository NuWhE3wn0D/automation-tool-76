import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        logger.error(f'failed to load {filepath}: {e}')
        return None

def save_json(data: Dict[str, Any], filepath: str) -> bool:
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        logger.error(f'failed to save {filepath}: {e}')
        return False

def sanitize_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data]
    return str(data) if data is not None else None
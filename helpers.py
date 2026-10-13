from typing import Any, Dict, List, Union, Optional
import json

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    return [data[i:i + size] for i in range(0, len(data), size)]

def filter_none_values(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}
import json
from typing import Any, Dict, List, Union


def clean_data(data: Any) -> Any:
    """Recursively strips string whitespace from nested structures."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [clean_data(item) for item in data]
    if isinstance(data, str):
        return data.strip()
    return data


def safe_load_json(data: str) -> Union[Dict, List, None]:
    """Safely parses JSON strings into Python objects."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return None


def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens nested dictionaries into single-level structures."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def validate_schema(data: Dict, required_keys: List[str]) -> bool:
    """Validates presence of required keys in dictionary."""
    return all(key in data for key in required_keys)
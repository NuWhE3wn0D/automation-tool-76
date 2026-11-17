from typing import Any, Optional, Dict

def validate_schema(data: Dict[str, Any], schema: Dict[str, type]) -> bool:
    if not isinstance(data, dict):
        return False
    return all(key in data and isinstance(data[key], val_type) for key, val_type in schema.items())

def sanitize_input(value: Any, default: Any = None) -> Any:
    if value is None:
        return default
    return str(value).strip()

def get_nested(data: Dict[str, Any], keys: str, delimiter: str = '.') -> Optional[Any]:
    parts = keys.split(delimiter)
    current = data
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return None

def is_non_empty_dict(data: Any) -> bool:
    return isinstance(data, dict) and bool(data)

def format_data(data: Dict[str, Any]) -> Dict[str, Any]:
    return {str(k).lower(): v for k, v in data.items()}
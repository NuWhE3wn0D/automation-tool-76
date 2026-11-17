from typing import Any, Dict, List, Optional

def validate_schema(data: Dict[str, Any], required_keys: List[str]) -> bool:
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def sanitize_input(value: Any) -> Optional[str]:
    if isinstance(value, str):
        return value.strip()
    return str(value).strip() if value is not None else None

def validate_numeric_range(value: Any, min_val: float, max_val: float) -> bool:
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False

def extract_field(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
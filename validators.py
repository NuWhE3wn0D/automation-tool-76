from typing import Any, Dict, List, Optional

def validate_schema(data: Dict[str, Any], required_keys: List[str]) -> bool:
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def sanitize_input(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float)):
        return value
    return None

def format_data(data: List[Dict[str, Any]], key: str) -> List[Any]:
    return [item.get(key) for item in data if key in item]

def filter_by_type(data: List[Any], target_type: type) -> List[Any]:
    return [item for item in data if isinstance(item, target_type)]

def validate_range(value: float, min_val: float, max_val: float) -> bool:
    return min_val <= value <= max_val

def extract_nested(data: Dict[str, Any], path: str) -> Optional[Any]:
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current
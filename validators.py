import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    return min_val <= value <= max_val

def validate_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and len(value.strip()) > 0

def validate_uuid(uuid_str: str) -> bool:
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    return bool(re.match(pattern, uuid_str, re.IGNORECASE))

def ensure_list(value: Any) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]

def sanitize_input(value: str) -> str:
    return value.strip().replace('\\', '').replace(';', '')
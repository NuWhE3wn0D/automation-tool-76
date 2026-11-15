import re
from typing import Any, Optional


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def sanitize_input(value: Any) -> str:
    if not isinstance(value, str):
        value = str(value)
    return value.strip()


def check_required_keys(data: dict, keys: list[str]) -> bool:
    return all(key in data for key in keys)


def enforce_type(value: Any, expected_type: type) -> Optional[Any]:
    if isinstance(value, expected_type):
        return value
    try:
        return expected_type(value)
    except (ValueError, TypeError):
        return None


def validate_numeric_range(value: Any, min_val: float, max_val: float) -> bool:
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False
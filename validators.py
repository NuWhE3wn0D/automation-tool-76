import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Validate email string format using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_positive_int(value: Any) -> bool:
    """Check if input is a positive integer."""
    return isinstance(value, int) and value > 0

def validate_non_empty_string(value: Any) -> bool:
    """Check if input is a string with content."""
    return isinstance(value, str) and len(value.strip()) > 0

def validate_config_key(key: str, allowed: list[str]) -> bool:
    """Verify config key exists in allowed list."""
    return key in allowed

def sanitize_input(data: str) -> str:
    """Strip whitespace and normalize string input."""
    return data.strip().lower()

def get_optional_value(data: dict[str, Any], key: str, default: Any = None) -> Optional[Any]:
    """Retrieve value from dict with fallback default."""
    return data.get(key, default)
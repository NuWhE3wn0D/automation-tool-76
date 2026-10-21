import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Validate email string format using regex."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_integer(value: Any, min_val: Optional[int] = None, max_val: Optional[int] = None) -> bool:
    """Validate if value is int and within optional bounds."""
    if not isinstance(value, int):
        return False
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True

def validate_required(value: Any) -> bool:
    """Check if input is not None and not empty."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict)) and not value:
        return False
    return True

def sanitize_input(value: str) -> str:
    """Remove non-alphanumeric characters from input string."""
    return re.sub(r'[^a-zA-Z0-9]', '', value)
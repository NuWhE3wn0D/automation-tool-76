import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Validate email string format using regex."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_port(port: Any) -> bool:
    """Validate integer port range 1-65535."""
    try:
        value = int(port)
        return 1 <= value <= 65535
    except (ValueError, TypeError):
        return False

def sanitize_input(value: Optional[str]) -> str:
    """Strip whitespace and return empty string if None."""
    return value.strip() if value else ""

def check_non_empty(value: Any) -> bool:
    """Verify input is not empty or null."""
    if isinstance(value, str):
        return len(value.strip()) > 0
    return value is not None
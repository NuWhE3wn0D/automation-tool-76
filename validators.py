from typing import Any, List, Optional


def validate_schema(data: dict, required_keys: List[str]) -> bool:
    """Validate that all required keys are present in the data dictionary."""
    return all(key in data for key in required_keys)


def validate_positive_integer(value: Any) -> bool:
    """Check if input is an integer greater than zero."""
    return isinstance(value, int) and value > 0


def sanitize_input(value: Optional[str]) -> str:
    """Strip whitespace and return empty string if input is None."""
    if value is None:
        return ""
    return value.strip()


def validate_email_format(email: str) -> bool:
    """Perform basic email format validation check."""
    if not isinstance(email, str) or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and all(len(p) > 0 for p in parts)


def validate_payload(data: Any, expected_type: type) -> bool:
    """Verify data matches the provided expected type."""
    return isinstance(data, expected_type)
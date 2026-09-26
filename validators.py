from typing import Any, Optional, Union


def validate_port(port: Any) -> int:
    """Validate that the provided port is within the valid range."""
    try:
        val = int(port)
        if 1 <= val <= 65535:
            return val
    except (ValueError, TypeError):
        pass
    raise ValueError(f"Invalid port number: {port}")


def validate_email(email: Any) -> str:
    """Check if the input string follows a basic email format."""
    if isinstance(email, str) and "@" in email and "." in email:
        return email
    raise ValueError(f"Invalid email format: {email}")


def check_non_empty(value: Optional[str]) -> str:
    """Ensure the provided string is not null or empty after stripping."""
    if value and isinstance(value, str) and value.strip():
        return value.strip()
    raise ValueError("Value cannot be empty")


def validate_timeout(timeout: Union[int, float]) -> float:
    """Verify that timeout is a positive numeric value."""
    if isinstance(timeout, (int, float)) and timeout >= 0:
        return float(timeout)
    raise ValueError(f"Invalid timeout value: {timeout}")
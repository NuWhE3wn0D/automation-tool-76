import os
import re
from typing import Any, Dict, List, Optional


def validate_file_path(path: str, must_exist: bool = True) -> bool:
    """Validate if a string is a valid file path and optionally exists.

    Args:
        path: Path string to validate.
        must_exist: Whether the path must exist on disk.

    Returns:
        True if valid, False otherwise.
    """
    if not path or not isinstance(path, str):
        return False
    if must_exist:
        return os.path.isfile(path)
    return True


def validate_email(email: str) -> bool:
    """Validate basic email format using regular expression.

    Args:
        email: Email address string to check.

    Returns:
        True if the email format is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def validate_config_dict(
    config: Dict[str, Any], required_keys: List[str]
) -> Optional[List[str]]:
    """Check if a dictionary contains all required top-level keys.

    Args:
        config: Configuration dictionary to validate.
        required_keys: List of keys that must be present.

    Returns:
        List of missing keys, or None if all required keys are present.
    """
    missing = [key for key in required_keys if key not in config]
    return missing if missing else None

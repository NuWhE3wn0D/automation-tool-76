"""Validation utilities for automation tool tasks and inputs."""

import re
from pathlib import Path
from typing import Any, Dict, List, Union


def validate_file_path(path: Union[str, Path], must_exist: bool = True) -> Path:
    """Validate and resolve a file path.

    Args:
        path: Path string or Path object to validate.
        must_exist: Whether the file must exist on disk.

    Returns:
        Resolved Path object.

    Raises:
        ValueError: If path is empty.
        FileNotFoundError: If must_exist is True and file does not exist.
    """
    if not path:
        raise ValueError("Path cannot be empty.")

    resolved_path = Path(path).resolve()
    if must_exist and not resolved_path.is_file():
        raise FileNotFoundError(f"File not found: {resolved_path}")

    return resolved_path


def validate_cron_expression(expression: str) -> bool:
    """Validate standard five-part cron expression syntax.

    Args:
        expression: Cron syntax string (e.g. '*/5 * * * *').

    Returns:
        True if valid syntax, False otherwise.
    """
    pattern = (
        r"^(\*|[0-9,\-\/]+)\s+(\*|[0-9,\-\/]+)\s+"
        r"(\*|[0-9,\-\/]+)\s+(\*|[0-9,\-\/]+)\s+(\*|[0-9,\-\/]+)$"
    )
    return bool(re.match(pattern, expression.strip()))


def validate_config_dict(config: Dict[str, Any], required_keys: List[str]) -> bool:
    """Check if required keys exist in the configuration dictionary.

    Args:
        config: Dictionary containing configuration settings.
        required_keys: List of key names that must be present.

    Returns:
        True if all required keys are present.

    Raises:
        KeyError: If missing one or more required keys.
    """
    missing = [key for key in required_keys if key not in config]
    if missing:
        raise KeyError(f"Missing required keys: {', '.join(missing)}")
    return True

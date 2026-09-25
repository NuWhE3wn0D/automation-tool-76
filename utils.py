import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class AutomationError(Exception):
    """Base exception for automation-tool-76."""

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Execute function with robust edge case handling."""
    try:
        if not callable(func):
            raise ValueError("Provided target is not callable")
        return func(*args, **kwargs)
    except (TypeError, ValueError) as e:
        logger.error(f"Input validation error in {func.__name__}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected runtime error in {func.__name__}: {e}")
    return None

def validate_payload(data: Any, expected_keys: list[str]) -> bool:
    """
    Strict validation of input structures.
    Returns True if dictionary contains all expected keys.
    """
    if not isinstance(data, dict):
        return False
    return all(key in data for key in expected_keys)

def get_nested(data: dict, keys: list[str], default: Any = None) -> Any:
    """
    Safe dictionary traversal for nested configuration access.
    """
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default
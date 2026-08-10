from typing import Any, Dict


def validate_integer(value: Any) -> int:
    """
    Validates that the provided value is an integer.

    Args:
        value (Any): The value to validate.

    Returns:
        int: The validated integer value.

    Raises:
        ValueError: If the value is not an integer.
    """
    if not isinstance(value, int):
        raise ValueError(f'Expected an integer, got {type(value).__name__}')
    return value


def validate_string(value: Any) -> str:
    """
    Validates that the provided value is a string.

    Args:
        value (Any): The value to validate.

    Returns:
        str: The validated string value.

    Raises:
        ValueError: If the value is not a string.
    """
    if not isinstance(value, str):
        raise ValueError(f'Expected a string, got {type(value).__name__}')
    return value


def validate_positive_integer(value: Any) -> int:
    """
    Validates that the provided value is a positive integer.

    Args:
        value (Any): The value to validate.

    Returns:
        int: The validated positive integer value.

    Raises:
        ValueError: If the value is not a positive integer.
    """
    validated_value = validate_integer(value)
    if validated_value <= 0:
        raise ValueError('Expected a positive integer')
    return validated_value

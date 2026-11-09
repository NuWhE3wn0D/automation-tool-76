from pathlib import Path
from typing import Any, Dict, List, Union


class ValidationError(Exception):
    """Raised when data validation fails."""
    pass


def validate_timeout(timeout: Union[int, float]) -> float:
    if timeout is None:
        raise ValidationError("Timeout value cannot be None")
    try:
        val = float(timeout)
    except (ValueError, TypeError) as err:
        raise ValidationError(f"Invalid timeout type: {timeout}") from err

    if val <= 0:
        raise ValidationError(f"Timeout must be positive, got {val}")
    if val > 3600:
        raise ValidationError(f"Timeout exceeds maximum limit of 3600s: {val}")
    return val


def validate_payload(data: Any, required_keys: List[str]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict payload, got {type(data).__name__}")
    if not data:
        raise ValidationError("Payload dictionary cannot be empty")

    missing = [key for key in required_keys if key not in data or data[key] is None]
    if missing:
        raise ValidationError(f"Missing or null required keys: {', '.join(missing)}")
    return data


def validate_file_path(path_str: str, must_exist: bool = False) -> Path:
    if not isinstance(path_str, (str, Path)) or not str(path_str).strip():
        raise ValidationError("File path must be a non-empty string or Path object")

    path = Path(path_str).resolve()
    if must_exist and not path.exists():
        raise ValidationError(f"Target path does not exist: {path}")
    return path


def validate_retry_count(count: Any, max_retries: int = 5) -> int:
    if count is None:
        return 0
    try:
        val = int(count)
    except (ValueError, TypeError) as err:
        raise ValidationError(f"Invalid retry count: {count}") from err

    if val < 0 or val > max_retries:
        raise ValidationError(f"Retry count must be between 0 and {max_retries}, got {val}")
    return val

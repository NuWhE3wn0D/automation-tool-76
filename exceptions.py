class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class DataProcessingError(AutomationError):
    """Raised when data transformation fails."""

class ValidationError(AutomationError):
    """Raised when input data fails validation."""

class ConfigurationError(AutomationError):
    """Raised when settings are invalid."""

def handle_exception(e: Exception) -> None:
    """Centralized exception logging utility."""
    import logging
    logger = logging.getLogger('automation-tool-76')
    logger.error(f"Error type: {type(e).__name__}, detail: {str(e)}")

def validate_data(data: dict, required_keys: list) -> None:
    """Ensure data contains all necessary keys."""
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")

if __name__ == "__main__":
    try:
        validate_data({}, ["id"])
    except ValidationError as e:
        handle_exception(e)
class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class ConfigurationError(AutomationError):
    """Raised when configuration values are invalid."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

class ProcessingError(AutomationError):
    """Raised during unexpected processing state."""

def raise_if_invalid(condition: bool, message: str) -> None:
    """Validate conditions and raise exception if False."""
    if not condition:
        raise ValidationError(message)

def handle_exception(exc: Exception) -> str:
    """Format exception message for logging."""
    return f"[{type(exc).__name__}] {str(exc)}"
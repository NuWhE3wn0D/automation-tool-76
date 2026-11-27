class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class ConfigurationError(AutomationError):
    """Raised when configuration values are invalid."""

class ProcessingError(AutomationError):
    """Raised during core task execution failures."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

class ResourceNotFoundError(AutomationError):
    """Raised when a required resource is missing."""

def handle_error(e: Exception) -> None:
    if isinstance(e, (ConfigurationError, ValidationError)):
        print(f"Critical setup failure: {e}")
    elif isinstance(e, ProcessingError):
        print(f"Task execution error: {e}")
    else:
        print(f"Unexpected system error: {e}")

if __name__ == "__main__":
    try:
        raise ValidationError("Invalid configuration schema")
    except AutomationError as err:
        handle_error(err)
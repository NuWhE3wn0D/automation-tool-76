class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class ConfigurationError(AutomationError):
    """Raised when configuration validation fails."""

class ConnectionTimeout(AutomationError):
    """Raised when external services exceed timeout."""

class ResourceNotFoundError(AutomationError):
    """Raised when a required resource is missing."""

class ValidationError(AutomationError):
    """Raised when input data fails schema validation."""

def handle_automation_error(error: Exception) -> None:
    if isinstance(error, (ConfigurationError, ValidationError)):
        print(f"Critical input error: {error}")
    elif isinstance(error, ConnectionTimeout):
        print(f"Retrying connection due to: {error}")
    else:
        print(f"Unexpected system failure: {error}")

def validate_resource(resource: any) -> None:
    if resource is None:
        raise ResourceNotFoundError("Required resource is null")
    if not isinstance(resource, dict):
        raise ValidationError("Invalid resource format provided")
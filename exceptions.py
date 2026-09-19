class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class ConfigurationError(AutomationError):
    """Raised when configuration values are invalid."""

class ProcessingError(AutomationError):
    """Raised when data processing operations fail."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

class ResourceNotFoundError(AutomationError):
    """Raised when a required resource is missing."""

class ConnectionTimeoutError(AutomationError):
    """Raised when network operations exceed limits."""

class StateInconsistencyError(AutomationError):
    """Raised when system state is invalid."""
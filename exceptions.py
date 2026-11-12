class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class ConfigurationError(AutomationError):
    """Raised when configuration validation fails."""

class ProcessorError(AutomationError):
    """Raised when data processing encounters an issue."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

class ExecutionError(AutomationError):
    """Raised during unexpected runtime execution failures."""

class ResourceNotFoundError(AutomationError):
    """Raised when a required resource is missing."""

class ConnectionError(AutomationError):
    """Raised when external service connectivity fails."""
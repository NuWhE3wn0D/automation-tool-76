class AutomationError(Exception):
    """Base exception for automation-tool-76."""

class ConfigurationError(AutomationError):
    """Raised when configuration settings are invalid."""

class ProcessingError(AutomationError):
    """Raised when data processing fails."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

class ConnectionError(AutomationError):
    """Raised when external services are unreachable."""

class TimeoutError(AutomationError):
    """Raised when operations exceed time limits."""

__all__ = [
    "AutomationError",
    "ConfigurationError",
    "ProcessingError",
    "ValidationError",
    "ConnectionError",
    "TimeoutError"
]
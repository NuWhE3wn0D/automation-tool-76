from typing import Optional

class AutomationError(Exception):
    """Base exception for automation-tool-76."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(AutomationError):
    """Raised when tool configuration is invalid."""

class ExecutionError(AutomationError):
    """Raised during automation process failures."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

def format_error(exc: AutomationError) -> str:
    """Returns formatted string representation of an error."""
    code_str = f" [{exc.code}]" if exc.code else ""
    return f"Error{code_str}: {str(exc)}"

class ConnectionTimeout(ExecutionError):
    """Raised on external service timeouts."""

class ResourceNotFoundError(AutomationError):
    """Raised when a required resource is missing."""
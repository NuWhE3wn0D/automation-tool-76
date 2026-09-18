from typing import Optional

class AutomationError(Exception):
    """Base exception for automation-tool-76."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(AutomationError):
    """Raised when tool configuration is invalid."""

class ProcessorError(AutomationError):
    """Raised during data processing failures."""

class ValidationError(AutomationError):
    """Raised when input validation fails."""

class NetworkError(AutomationError):
    """Raised during connectivity or API issues."""

def format_error(error: AutomationError) -> str:
    """Format exception details for logging."""
    base_msg = str(error)
    code_msg = f" (Code: {error.code})" if error.code else ""
    return f"{type(error).__name__}: {base_msg}{code_msg}"
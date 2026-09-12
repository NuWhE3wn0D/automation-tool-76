from typing import Optional

class AutomationError(Exception):
    """Base exception for automation-tool-76."""
    pass

class ConfigurationError(AutomationError):
    """Raised when configuration settings are invalid."""
    def __init__(self, message: str, field: Optional[str] = None) -> None:
        self.field = field
        super().__init__(f"{message} (field: {field})" if field else message)

class ExecutionError(AutomationError):
    """Raised when a process execution fails."""
    def __init__(self, message: str, exit_code: int) -> None:
        self.exit_code = exit_code
        super().__init__(f"{message} with exit code {exit_code}")

class ValidationError(AutomationError):
    """Raised when data validation fails."""
    def __init__(self, message: str, data: any = None) -> None:
        self.data = data
        super().__init__(message)

class TimeoutError(AutomationError):
    """Raised when an operation exceeds time limits."""
    def __init__(self, message: str, timeout: float) -> None:
        self.timeout = timeout
        super().__init__(f"{message} after {timeout} seconds")
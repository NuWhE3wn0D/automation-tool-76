from typing import Optional

class AutomationError(Exception):
    """Base exception for automation-tool-76."""
    pass

class ConfigurationError(AutomationError):
    """Raised when configuration settings are invalid."""
    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        self.config_key = config_key
        super().__init__(f"{message} (key: {config_key})" if config_key else message)

class ExecutionError(AutomationError):
    """Raised when an automation step fails execution."""
    def __init__(self, message: str, exit_code: int = 1) -> None:
        self.exit_code = exit_code
        super().__init__(f"{message} (code: {exit_code})")

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(f"Validation failed for {field}: {reason}")
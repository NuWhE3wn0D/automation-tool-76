"""Custom exceptions for automation-tool-76."""

from typing import Optional


class AutomationError(Exception):
    """Base exception for all automation tool errors."""

    def __init__(self, message: str, details: Optional[str] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: Optional[str] = details

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} (Details: {self.details})"
        return self.message


class ConfigurationError(AutomationError):
    """Raised when there is an issue with the configuration."""


class ValidationError(AutomationError):
    """Raised when input validation fails."""


class ExecutionError(AutomationError):
    """Raised when a task execution fails."""

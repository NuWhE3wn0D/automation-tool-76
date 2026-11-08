"""Custom exceptions for the automation tool framework."""

from typing import Any, Optional


class AutomationError(Exception):
    """Base exception class for all automation tool errors."""

    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: Optional[Any] = details

    def __str__(self) -> str:
        if self.details is not None:
            return f"{self.message} (details: {self.details})"
        return self.message


class ConfigurationError(AutomationError):
    """Raised when configuration validation or loading fails."""

    pass


class TaskExecutionError(AutomationError):
    """Raised when an automated task execution fails."""

    def __init__(
        self, message: str, task_name: str, details: Optional[Any] = None
    ) -> None:
        super().__init__(message, details)
        self.task_name: str = task_name

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"[Task: {self.task_name}] {base_str}"


class ValidationError(AutomationError):
    """Raised when input data or schema validation fails."""

    pass


class ResourceNotFoundError(AutomationError):
    """Raised when a required external resource or file is missing."""

    def __init__(
        self, message: str, resource_path: str, details: Optional[Any] = None
    ) -> None:
        super().__init__(message, details)
        self.resource_path: str = resource_path

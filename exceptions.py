"""Custom exception classes for the automation tool framework."""

from typing import Any, Optional


class AutomationError(Exception):
    """Base exception for all automation framework errors."""

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: dict[str, Any] = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class ConfigurationError(AutomationError):
    """Raised when there is an issue with configuration settings."""


class TaskExecutionError(AutomationError):
    """Raised when an automated task fails during execution."""

    def __init__(
        self,
        message: str,
        task_name: str,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, details)
        self.task_name: str = task_name

    def __str__(self) -> str:
        base_msg = super().__str__()
        return f"[Task: {self.task_name}] {base_msg}"


class ValidationError(AutomationError):
    """Raised when input data or parameter validation fails."""


class TaskTimeoutError(TaskExecutionError):
    """Raised when an execution task exceeds its configured time limit."""

    def __init__(
        self,
        message: str,
        task_name: str,
        timeout_seconds: float,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, task_name, details)
        self.timeout_seconds: float = timeout_seconds

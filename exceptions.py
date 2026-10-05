class AutomationError(Exception):
    """Base exception for automation-tool-76."""


class ValidationError(AutomationError):
    """Raised when input validation fails."""


class ConfigurationError(AutomationError):
    """Raised when settings are invalid."""


class ExecutionError(AutomationError):
    """Raised when a process operation fails."""


def raise_if_none(value, message="Value cannot be None"):
    if value is None:
        raise ValidationError(message)
    return value


def handle_execution(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise ExecutionError(f"Operation failed: {str(e)}") from e
    return wrapper
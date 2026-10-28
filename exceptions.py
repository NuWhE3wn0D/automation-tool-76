class AutomationError(Exception):
    """Base exception for automation-tool-76."""


class ValidationError(AutomationError):
    """Raised when input validation fails."""


class ConfigurationError(AutomationError):
    """Raised for missing or invalid configuration settings."""


class ResourceNotFoundError(AutomationError):
    """Raised when a required resource is missing."""


def raise_if_none(value, message):
    if value is None:
        raise ResourceNotFoundError(message)


def validate_condition(condition, message):
    if not condition:
        raise ValidationError(message)
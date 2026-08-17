class CustomError(Exception):
    """Exception raised for custom errors."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource: str) -> None:
        super().__init__(f'{resource} not found')

class ValidationError(CustomError):
    """Exception raised when validation fails."""
    def __init__(self, field: str, errors: list) -> None:
        self.field = field
        self.errors = errors
        super().__init__(f'Validation failed for {field}: {
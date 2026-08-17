class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NotFoundError(CustomError):
    pass

class ValidationError(CustomError):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field

class PermissionError(CustomError):
    pass

def handle_exception(e):
    if isinstance(e, CustomError):
        return {'error': e.message}
    return {'error': 'An unexpected error occurred.'}
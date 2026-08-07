class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message='Item not found'):
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    def __init__(self, message='Validation failed'):
        self.message = message
        super().__init__(self.message)

class PermissionDeniedError(CustomError):
    def __init__(self, message='Permission denied'):
        self.message = message
        super().__init__(self.message)

class TimeoutError(CustomError):
    def __init__(self, message='Operation timed out'):
        self.message = message
        super().__init__(self.message)

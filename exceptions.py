class CustomError(Exception):
    pass

class ValidationError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class ConnectionError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class FileNotFoundError(CustomError):
    def __init__(self, filename):
        message = f'File {filename} not found'
        super().__init__(message)

class PermissionDeniedError(CustomError):
    def __init__(self, filename):
        message = f'Permission denied for {filename}'
        super().__init__(message)
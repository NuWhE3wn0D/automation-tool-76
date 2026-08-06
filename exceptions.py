class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    pass

class ProcessingError(CustomError):
    pass

class ConfigurationError(CustomError):
    pass

class NotFoundError(CustomError):
    pass

class PermissionError(CustomError):
    pass

class NetworkError(CustomError):
    pass

class TimeoutError(NetworkError):
    pass

class FileNotFoundError(Exception):
    def __init__(self, filepath):
        self.filepath = filepath
        super().__init__(f'File not found: {self.filepath}')
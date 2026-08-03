class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ValidationError(CustomError):
    pass

class ProcessingError(CustomError):
    pass

class ConfigurationError(CustomError):
    pass

class FileNotFoundError(CustomError):
    pass

class TimeoutError(CustomError):
    pass

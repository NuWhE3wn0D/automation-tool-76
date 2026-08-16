class CustomError(Exception):
    pass

class ValidationError(CustomError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ProcessingError(CustomError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConfigError(CustomError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    def __init__(self, resource):
        self.message = f'{resource} not found'
        super().__init__(self.message)
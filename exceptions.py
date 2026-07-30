class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message="Not Found"): 
        super().__init__(message)

class ValidationError(CustomError):
    def __init__(self, field, message="Invalid value"): 
        self.field = field
        super().__init__(f"{field}: {message}")

class AuthError(CustomError):
    def __init__(self, message="Authentication failed"): 
        super().__init__(message)

class PermissionError(CustomError):
    def __init__(self, message="Permission denied"): 
        super().__init__(message)

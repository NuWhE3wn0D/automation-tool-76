class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ValidationError(CustomException):
    def __init__(self, field, message='Invalid value'):
        super().__init__(message)
        self.field = field

class ResourceNotFound(CustomException):
    def __init__(self, resource):
        message = f'Resource {resource} not found'
        super().__init__(message)
        self.resource = resource

class UnauthorizedAccess(CustomException):
    def __init__(self, user):
        message = f'Unauthorized access for user {user}'
        super().__init__(message)
        self.user = user
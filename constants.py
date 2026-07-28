VERSION = '1.0.0'
DEFAULT_CONFIG = {
    'timeout': 30,
    'max_retries': 5,
    'base_url': 'https://api.example.com',
    'log_level': 'INFO',
}
HTTP_STATUS_CODES = {
    200: 'OK',
    400: 'Bad Request',
    404: 'Not Found',
    500: 'Internal Server Error',
}
ERROR_MESSAGES = {
    'network_error': 'Network connectivity issue.',
    'timeout_error': 'Operation timed out.',
    'response_error': 'Invalid response from server.',
}
SUPPORTED_FILE_TYPES = ['csv', 'json', 'xml']
MAX_FILE_SIZE_MB = 10

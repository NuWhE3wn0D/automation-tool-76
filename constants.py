AUTH_TOKEN = 'your_auth_token'

BASE_URL = 'https://api.example.com'

TIMEOUT = 30

RETRY_LIMIT = 3

HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'automation-tool-76'
}

STATUS_CODES = {
    'OK': 200,
    'CREATED': 201,
    'NO_CONTENT': 204,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'INTERNAL_SERVER_ERROR': 500
}

DEFAULT_CONFIG = {
    'log_level': 'INFO',
    'max_retries': 5,
    'timeout': 60
}

SUPPORTED_FORMATS = ['json', 'xml', 'csv']
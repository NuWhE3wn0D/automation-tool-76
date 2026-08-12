DATABASE_URI = 'sqlite:///example.db'

API_KEY = 'your_api_key_here'

TIMEOUT_SECONDS = 30

MAX_RETRIES = 5

DEFAULT_THEME = 'light'

SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de']

LOG_LEVEL = 'INFO'

FILE_PATH = '/path/to/your/file'

SMTP_SERVER = 'smtp.example.com'

SMTP_PORT = 587

EMAIL_ADDRESS = 'example@example.com'

EMAIL_PASSWORD = 'password_here'

def get_timeout():
    return TIMEOUT_SECONDS

def get_max_retries():
    return MAX_RETRIES

def get_database_uri():
    return DATABASE_URI

def get_supported_languages():
    return SUPPORTED_LANGUAGES
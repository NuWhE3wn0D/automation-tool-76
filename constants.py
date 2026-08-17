from typing import Final

API_URL: Final[str] = 'https://api.example.com'
TIMEOUT: Final[int] = 30
RETRY_COUNT: Final[int] = 5

class StatusCodes:
    SUCCESS: Final[int] = 200
    NOT_FOUND: Final[int] = 404
    SERVER_ERROR: Final[int] = 500
    
    @staticmethod
    def is_success(code: int) -> bool:
        """Check if the status code is successful."""
        return code == StatusCodes.SUCCESS

    @staticmethod
    def is_client_error(code: int) -> bool:
        """Check if the status code is a client error."""
        return 400 <= code < 500

    @staticmethod
    def is_server_error(code: int) -> bool:
        """Check if the status code is a server error."""
        return 500 <= code < 600

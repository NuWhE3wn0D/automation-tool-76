from typing import Final

TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3
DEFAULT_ENCODING: Final[str] = 'utf-8'

LOG_LEVELS: Final[dict[str, int]] = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50,
}

SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = ('.json', '.yaml', '.csv', '.txt')

class AppDefaults:
    """Collection of application default configurations."""
    API_VERSION: Final[str] = "v1.0.0"
    MAX_WORKERS: Final[int] = 4
    BASE_URL: Final[str] = "https://api.automation-tool-76.local"

    @classmethod
    def get_headers(cls) -> dict[str, str]:
        """Return default request headers."""
        return {
            "Content-Type": "application/json",
            "X-App-Version": cls.API_VERSION
        }
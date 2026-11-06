from typing import Final, Dict, List

TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3
API_BASE_URL: Final[str] = "https://api.automation-tool-76.io"
SUPPORTED_EXTENSIONS: Final[List[str]] = [".json", ".yaml", ".toml"]

STATUS_CODES: Final[Dict[int, str]] = {
    200: "OK",
    201: "CREATED",
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    404: "NOT_FOUND",
    500: "SERVER_ERROR",
}

def get_timeout() -> int:
    """Return the configured timeout value."""
    return TIMEOUT_SECONDS

def is_supported(extension: str) -> bool:
    """Check if the provided file extension is allowed."""
    return extension.lower() in SUPPORTED_EXTENSIONS
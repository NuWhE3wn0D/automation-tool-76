from typing import Final, Dict, List

TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 5

DEFAULT_HEADERS: Final[Dict[str, str]] = {
    "Content-Type": "application/json",
    "User-Agent": "automation-tool-76/1.0.0"
}

SUPPORTED_OPERATIONS: Final[List[str]] = [
    "sync",
    "validate",
    "archive"
]

def get_version() -> str:
    """Return current automation-tool-76 version string."""
    return "1.0.0"

def get_retry_backoff() -> List[int]:
    """Return predefined exponential backoff intervals in seconds."""
    return [1, 2, 4, 8, 16]
from typing import Final, Dict, Any
import os

CACHE_SIZE: Final[int] = 1024
TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

ENV_PREFIX: Final[str] = "AUTOTOOL_"

SETTINGS: Final[Dict[str, Any]] = {
    "workers": int(os.getenv(f"{ENV_PREFIX}WORKERS", "4")),
    "buffer_size": 8192,
    "log_level": "INFO",
    "enable_optimization": True
}

RESERVED_KEYS: Final[set] = {"id", "status", "timestamp", "metadata"}

def get_optimized_buffer_size() -> int:
    return SETTINGS["buffer_size"] if SETTINGS["enable_optimization"] else 4096

class AppConfig:
    __slots__ = ("cache_size", "timeout")

    def __init__(self) -> None:
        self.cache_size = CACHE_SIZE
        self.timeout = TIMEOUT
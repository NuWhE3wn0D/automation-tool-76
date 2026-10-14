import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

SUPPORTED_EXTENSIONS = {".json", ".yaml", ".csv"}

ENV_VARS = {
    "API_KEY": "AUTO_API_KEY",
    "DB_URL": "AUTO_DB_URL"
}

RETRY_BACKOFF_FACTOR = 0.5

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_config_path(filename: str) -> Path:
    return BASE_DIR / "config" / filename

if __name__ == "__main__":
    LOG_DIR.mkdir(exist_ok=True)
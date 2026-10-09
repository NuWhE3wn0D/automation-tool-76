import os
from pathlib import Path
from typing import Dict, Any

class Settings:
    def __init__(self) -> None:
        self.base_dir = Path(__file__).resolve().parent
        self.env = os.getenv("APP_ENV", "development")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.max_retries = int(os.getenv("MAX_RETRIES", "3"))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "env": self.env,
            "log_level": self.log_level,
            "max_retries": self.max_retries
        }

def get_config() -> Settings:
    return Settings()

config = get_config()
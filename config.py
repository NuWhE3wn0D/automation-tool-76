import os
from pathlib import Path
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent

def load_environment_config() -> Dict[str, Any]:
    return {
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "timeout": int(os.getenv("TIMEOUT", "30")),
        "max_retries": int(os.getenv("MAX_RETRIES", "3")),
        "output_dir": BASE_DIR / "output"
    }

class Settings:
    def __init__(self):
        self.env = load_environment_config()

    def get(self, key: str, default: Any = None) -> Any:
        return self.env.get(key, default)

    @property
    def storage_path(self) -> Path:
        path = self.env.get("output_dir")
        path.mkdir(parents=True, exist_ok=True)
        return path

app_settings = Settings()
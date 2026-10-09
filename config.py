import os
from typing import Dict, Any
from pathlib import Path

class AppConfig:
    BASE_DIR: Path = Path(__file__).resolve().parent
    ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = "INFO" if ENV == "production" else "DEBUG"
    TIMEOUT: int = int(os.getenv("APP_TIMEOUT", "30"))

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        return {
            "env": cls.ENV,
            "log_level": cls.LOG_LEVEL,
            "timeout": cls.TIMEOUT
        }

def load_settings() -> Dict[str, Any]:
    return AppConfig.to_dict()

if __name__ == "__main__":
    print(load_settings())
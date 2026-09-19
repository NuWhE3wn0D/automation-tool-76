import os
from typing import Dict, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    env: str = os.getenv("APP_ENV", "production")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    timeout: int = int(os.getenv("TIMEOUT", 30))

def load_configuration() -> Config:
    return Config()

class Settings:
    _settings: Dict[str, Any] = {
        "version": "1.0.0",
        "retries": 3,
        "base_path": "/var/lib/automation"
    }

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        return cls._settings.get(key, default)

def validate_env() -> bool:
    required = ["APP_ENV"]
    return all(os.getenv(var) for var in required)
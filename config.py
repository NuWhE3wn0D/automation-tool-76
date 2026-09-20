import json
import os
from typing import Any, Dict


class Config:
    DEFAULT_CONFIG = {
        "host": "127.0.0.1",
        "port": 8080,
        "debug": False,
        "timeout": 30,
        "retry_limit": 3,
    }

    def __init__(self, config_path: str | None = None) -> None:
        self._config: Dict[str, Any] = self.DEFAULT_CONFIG.copy()
        if config_path:
            self.load_from_file(config_path)
        self._load_from_env()

    def load_from_file(self, path: str) -> None:
        if not os.path.exists(path):
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                if isinstance(file_data, dict):
                    self._config.update(file_data)
        except (json.JSONDecodeError, OSError):
            pass

    def _load_from_env(self) -> None:
        for key in self._config:
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                self._config[key] = self._cast_value(val, type(self._config[key]))

    @staticmethod
    def _cast_value(value: str, target_type: type) -> Any:
        if target_type is bool:
            return value.lower() in ("true", "1", "yes")
        try:
            return target_type(value)
        except ValueError:
            return value

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def __getattr__(self, name: str) -> Any:
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"'Config' object has no attribute '{name}'")

import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "log_level": "INFO",
    "enabled": True
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.settings
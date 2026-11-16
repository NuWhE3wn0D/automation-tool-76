import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "verbose": False,
    "log_path": "/var/log/automation.log"
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                try:
                    user_data = json.load(f)
                    self.settings.update(user_data)
                except json.JSONDecodeError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(settings={self.settings})"
import json
import os
from typing import Any, Dict

DEFAULTS = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return DEFAULTS
        try:
            with open(self.filepath, "r") as f:
                user_config = json.load(f)
            return {**DEFAULTS, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULTS

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    @property
    def all(self) -> Dict[str, Any]:
        return self.data.copy()
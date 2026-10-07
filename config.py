import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "debug": False
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.data = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_data = json.load(f)
                    self.data.update(user_data)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def save(self) -> None:
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)
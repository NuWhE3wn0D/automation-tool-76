import json
import os
from typing import Any, Dict

class ConfigLoader:
    DEFAULTS = {
        "port": 8080,
        "host": "127.0.0.1",
        "debug": False
    }

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.DEFAULTS.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.config
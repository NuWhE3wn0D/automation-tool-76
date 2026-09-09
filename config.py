import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "timeout": 30
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
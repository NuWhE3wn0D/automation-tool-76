import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return self.config

        try:
            with open(self.filepath, "r") as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def reload(self) -> Dict[str, Any]:
        return self.load()
import json
import os
from typing import Any, Dict

DEFAULTS = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

def load_config(path: str) -> Dict[str, Any]:
    config = DEFAULTS.copy()
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
    return config

class ConfigManager:
    def __init__(self, path: str = "config.json"):
        self._config = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()
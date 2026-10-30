import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "timeout": 30,
    "retry_count": 3
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return self.config

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
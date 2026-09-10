import json
import os
from typing import Any, Dict

DEFAULTS = {
    "timeout": 30,
    "retries": 3,
    "debug": False
}

class ConfigLoader:
    def __init__(self, file_path: str = "config.json"):
        self.file_path = file_path

    def load(self) -> Dict[str, Any]:
        config = DEFAULTS.copy()
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    user_config = json.load(f)
                    config.update(user_config)
                except json.JSONDecodeError:
                    pass
        return config

def get_config(path: str = "config.json") -> Dict[str, Any]:
    return ConfigLoader(path).load()
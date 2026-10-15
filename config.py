import json
import os
from typing import Any, Dict

DEFAULTS = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

def load_config(filepath: str) -> Dict[str, Any]:
    config = DEFAULTS.copy()
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
    return config

def get_setting(key: str, filepath: str = "config.json") -> Any:
    config = load_config(filepath)
    return config.get(key, DEFAULTS.get(key))
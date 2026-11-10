import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "retries": 3,
    "timeout": 30,
    "log_level": "INFO",
    "enabled": True
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    if not os.path.exists(path):
        return config

    try:
        with open(path, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def get_config_value(key: str, path: str = "config.json") -> Any:
    config = load_config(path)
    return config.get(key, DEFAULT_CONFIG.get(key))
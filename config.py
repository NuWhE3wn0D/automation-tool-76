import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    config_path = Path(path)

    if config_path.exists():
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)

    return config

def get_config_value(key: str, default: Any = None) -> Any:
    config = load_config()
    return config.get(key, default)
import os
import json
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULTS = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "output_dir": "output",
    "batch_size": 100,
}

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    config = DEFAULTS.copy()
    if config_path is None:
        config_path = os.getenv("CONFIG_PATH", "config.json")
    path = Path(config_path)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            file_config = json.load(f)
            config.update(file_config)
    for key in list(config.keys()):
        env_key = f"APP_{key.upper()}"
        if env_key in os.environ:
            value = os.environ[env_key]
            if isinstance(config[key], int):
                try:
                    config[key] = int(value)
                except ValueError:
                    pass
            elif isinstance(config[key], float):
                try:
                    config[key] = float(value)
                except ValueError:
                    pass
            else:
                config[key] = value
    return config

def get_config_value(key: str, config: Optional[Dict[str, Any]] = None) -> Any:
    if config is None:
        config = load_config()
    return config.get(key, DEFAULTS.get(key))
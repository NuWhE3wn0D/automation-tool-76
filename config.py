import json
import os
from typing import Any, Dict

DEFAULTS: Dict[str, Any] = {
    "debug": False,
    "timeout": 30,
    "max_retries": 3,
    "output_dir": "./output",
    "log_level": "INFO",
    "batch_size": 100,
}

def load_config(config_path: str = None) -> Dict[str, Any]:
    config: Dict[str, Any] = DEFAULTS.copy()
    if config_path is not None and os.path.exists(config_path):
        with open(config_path, encoding="utf-8") as f:
            loaded = json.load(f)
            if isinstance(loaded, dict):
                for k, v in loaded.items():
                    if k in config:
                        config[k] = v
    for key in list(config.keys()):
        env_key = "AUTOMATION_" + key.upper()
        if env_key in os.environ:
            env_val = os.environ[env_key]
            orig = config[key]
            if isinstance(orig, bool):
                config[key] = env_val.lower() in {"true", "1", "yes"}
            elif isinstance(orig, int):
                try:
                    config[key] = int(env_val)
                except ValueError:
                    pass
            else:
                config[key] = env_val
    return config
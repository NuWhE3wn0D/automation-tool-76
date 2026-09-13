import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 8080,
    "debug": False,
    "timeout": 30,
    "retry_limit": 3,
    "output_dir": "./output"
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass
        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        for key, default_val in DEFAULT_CONFIG.items():
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                env_val = os.environ[env_key]
                val_type = type(default_val)
                try:
                    if val_type is bool:
                        self.config[key] = env_val.lower() in ("true", "1", "yes", "on")
                    else:
                        self.config[key] = val_type(env_val)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
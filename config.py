import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any], config_path: str = "config.json"):
        self.config_path = config_path
        self.config = default_config
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def save(self) -> None:
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

def load_settings(defaults: Dict[str, Any], path: str = "config.json") -> ConfigLoader:
    return ConfigLoader(defaults, path)
import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, config_path: str, defaults: Dict[str, Any]):
        self.config_path = config_path
        self.defaults = defaults
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return self.defaults
        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
                return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str) -> Any:
        return self.config.get(key)

def get_config(path: str, defaults: Dict[str, Any]) -> ConfigLoader:
    return ConfigLoader(path, defaults)
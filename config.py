import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, config_path: str, defaults: Dict[str, Any] = None):
        self.config_path = config_path
        self.defaults = defaults or {}
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

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def save(self, data: Dict[str, Any]) -> None:
        self.config.update(data)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)
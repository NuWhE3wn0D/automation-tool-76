import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None, env_prefix: str = "APP_"):
        self.config = defaults or {}
        self.env_prefix = env_prefix

    def load_from_json(self, file_path: str) -> None:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.config.update(json.load(f))

    def load_from_env(self) -> None:
        for key in os.environ:
            if key.startswith(self.env_prefix):
                config_key = key[len(self.env_prefix):].lower()
                self.config[config_key] = os.environ[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.config.copy()
import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self._config = defaults

    def load_from_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            return
        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self._config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

def get_app_config(path: str = 'config.json') -> ConfigLoader:
    defaults = {
        'host': '127.0.0.1',
        'port': 8080,
        'debug': False
    }
    loader = ConfigLoader(defaults)
    loader.load_from_file(path)
    return loader
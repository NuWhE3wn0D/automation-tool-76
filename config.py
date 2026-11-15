import json
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, file_path: str) -> Dict[str, Any]:
        path = Path(file_path)
        if not path.exists():
            return self.defaults

        try:
            with open(path, "r") as f:
                user_config = json.load(f)
            return {**self.defaults, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.defaults

def get_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    loader = ConfigLoader(defaults)
    return loader.load(path)
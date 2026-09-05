import json
import os
from typing import Any, Dict


class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config
        self.config = default_config.copy()

    def load(self, filepath: str) -> Dict[str, Any]:
        if not os.path.exists(filepath):
            return self.config

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self._merge(self.config, user_config)
        except (json.JSONDecodeError, OSError):
            pass

        return self.config

    def _merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        for key, value in update.items():
            if (
                isinstance(value, dict)
                and key in base
                and isinstance(base[key], dict)
            ):
                self._merge(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

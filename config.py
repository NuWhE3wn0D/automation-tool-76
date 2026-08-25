import json
import os
from typing import Any, Dict, Optional

class Config:
    def __init__(self, defaults: Dict[str, Any], config_file: Optional[str] = None):
        self._defaults = defaults
        self._config_file = config_file or "config.json"
        self._data: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        data = self._defaults.copy()
        if os.path.exists(self._config_file):
            try:
                with open(self._config_file, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        data.update(file_data)
            except (json.JSONDecodeError, IOError, OSError):
                pass
        for key, value in list(os.environ.items()):
            if key.startswith("CONFIG_"):
                env_key = key[7:].lower().replace("_", ".")
                parts = env_key.split(".")
                try:
                    parsed_value = json.loads(value)
                except (json.JSONDecodeError, TypeError, ValueError):
                    parsed_value = value
                current = data
                for part in parts[:-1]:
                    if part not in current or not isinstance(current.get(part), dict):
                        current[part] = {}
                    current = current[part]
                current[parts[-1]] = parsed_value
        return data

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        keys = key.split(".")
        value = self._data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def __getitem__(self, key: str) -> Any:
        val = self.get(key)
        if val is None:
            raise KeyError(key)
        return val

    def __contains__(self, key: str) -> bool:
        return self.get(key) is not None

    def update(self, new_values: Dict[str, Any]) -> None:
        self._data.update(new_values)

    def save(self) -> None:
        with open(self._config_file, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2)

    def all(self) -> Dict[str, Any]:
        return self._data.copy()
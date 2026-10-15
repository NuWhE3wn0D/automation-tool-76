import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-76",
    "version": "1.0.0",
    "debug": False,
    "max_threads": 4,
    "timeout": 30,
    "log_level": "INFO",
    "output_dir": "./output",
}


class ConfigLoader:
    def __init__(self, config_path: str | None = None) -> None:
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        if self.config_path and os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                self._config.update(file_config)

        for key in self._config:
            env_var = f"APP_{key.upper()}"
            if env_var in os.environ:
                val = os.environ[env_var]
                if val.lower() in ("true", "false"):
                    self._config[key] = val.lower() == "true"
                elif val.isdigit():
                    self._config[key] = int(val)
                else:
                    self._config[key] = val

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()

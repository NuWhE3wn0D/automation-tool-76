import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-76",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "output_dir": "./output",
}


class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None):
        self._config = DEFAULT_CONFIG.copy()
        if config_path:
            self.load_from_file(config_path)
        self.load_from_env()

    def load_from_file(self, path: str) -> None:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self._config.update(data)

    def load_from_env(self, prefix: str = "APP_") -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                if value.isdigit():
                    parsed_val: Any = int(value)
                elif value.lower() in ("true", "false"):
                    parsed_val = value.lower() == "true"
                else:
                    parsed_val = value
                self._config[config_key] = parsed_val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()

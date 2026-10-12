import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-76",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "max_retries": 3,
    "output_dir": "./output",
}


class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or os.getenv("APP_CONFIG_PATH", "config.json")
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass

        self._apply_env_overrides()
        return self._config

    def _apply_env_overrides(self) -> None:
        env_mappings = {
            "APP_DEBUG": ("debug", lambda x: x.lower() in ("true", "1", "yes")),
            "APP_LOG_LEVEL": ("log_level", str),
            "APP_TIMEOUT": ("timeout", int),
            "APP_MAX_RETRIES": ("max_retries", int),
            "APP_OUTPUT_DIR": ("output_dir", str),
        }
        for env_var, (config_key, transform) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    self._config[config_key] = transform(val)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        return self._config

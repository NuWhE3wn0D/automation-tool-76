import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "timeout": 30,
    "retries": 3,
    "debug": False,
    "log_level": "INFO",
    "output_dir": "./output"
}

class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        if self.config_path:
            self.load()

    def load(self) -> Dict[str, Any]:
        if not self.config_path or not os.path.exists(self.config_path):
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self.config.update(user_config)
        except (json.JSONDecodeError, OSError):
            pass
        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

import os
import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

class ConfigError(Exception):
    pass

def load_config(path: str) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        raise ConfigError(f"config file missing: {path}")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("invalid config format: expected dict")
            return data
    except (json.JSONDecodeError, PermissionError, ValueError) as e:
        logger.error(f"config loading failure: {e}")
        raise ConfigError(f"configuration processing error: {e}") from e

def get_env_variable(key: str, default: Any = None) -> Any:
    value = os.getenv(key)
    if value is None:
        if default is not None:
            return default
        raise ConfigError(f"missing environment variable: {key}")
    return value
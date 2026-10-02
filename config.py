import os
import logging
from typing import Any, Dict

class ConfigError(Exception):
    pass

def load_config(path: str) -> Dict[str, Any]:
    if not path or not os.path.exists(path):
        raise ConfigError(f"configuration file not found: {path}")

    try:
        with open(path, 'r') as f:
            data = f.read()
            if not data.strip():
                raise ConfigError("empty configuration file")
            return {"content": data}
    except PermissionError:
        raise ConfigError(f"insufficient permissions for: {path}")
    except Exception as e:
        raise ConfigError(f"unexpected read error: {str(e)}")

def get_setting(config: Dict[str, Any], key: str, default: Any = None) -> Any:
    try:
        return config.get(key, default)
    except AttributeError:
        return default

def validate_env(required_vars: list) -> None:
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise ConfigError(f"missing environment variables: {', '.join(missing)}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        validate_env(["APP_ENV"])
    except ConfigError as e:
        logging.error(f"config initialization failure: {e}")
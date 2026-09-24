import os
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class ConfigError(Exception):
    pass

def load_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise ConfigError(f"missing config file: {path}")
    
    try:
        with open(path, 'r') as f:
            data = f.read().strip()
            if not data:
                raise ConfigError("config file is empty")
            
            import json
            config = json.loads(data)
            
            if not isinstance(config, dict):
                raise ConfigError("invalid config structure: expected dict")
            
            return config
    except json.JSONDecodeError as e:
        raise ConfigError(f"malformed json: {e.msg}") from e
    except Exception as e:
        logger.error(f"unexpected failure: {e}")
        raise ConfigError("critical configuration read failure") from e

def get_setting(config: Dict[str, Any], key: str, default: Any = None) -> Any:
    try:
        return config.get(key, default)
    except AttributeError:
        return default
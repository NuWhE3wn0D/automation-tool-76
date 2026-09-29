import os
import logging
from typing import Any, Optional

class ConfigError(Exception):
    pass

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    try:
        value = os.environ.get(key, default)
        if value is None:
            raise ConfigError(f'missing required environment variable: {key}')
        return value
    except Exception as e:
        logging.error(f'failed to retrieve config: {key}')
        raise ConfigError(f'config access failure for {key}') from e

class AppConfig:
    def __init__(self) -> None:
        self.db_url = get_env_variable('DB_URL')
        self.timeout = int(get_env_variable('TIMEOUT', '30'))

    def validate(self) -> bool:
        if not self.db_url.startswith('postgresql://'):
            raise ConfigError('invalid database protocol')
        if self.timeout <= 0:
            raise ConfigError('timeout must be a positive integer')
        return True

def load_configuration() -> AppConfig:
    try:
        config = AppConfig()
        config.validate()
        return config
    except (ValueError, ConfigError) as e:
        logging.critical(f'configuration loading aborted: {e}')
        raise
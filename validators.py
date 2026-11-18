import re
from typing import Any

class DataValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_integer(value: Any, min_val: int = 0, max_val: int = 100) -> bool:
        try:
            val = int(value)
            return min_val <= val <= max_val
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_config_key(key: str) -> bool:
        return bool(re.match(r'^[a-z_][a-z0-9_]*$', key))

def clean_input(value: Any) -> str:
    if not isinstance(value, str):
        return ''
    return value.strip().lower()

class ValidationError(Exception):
    pass
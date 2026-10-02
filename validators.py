import re
from typing import Any, Optional

class DataValidator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        return min_val <= value <= max_val

    @staticmethod
    def sanitize_input(data: str) -> str:
        return data.strip().replace('<', '').replace('>', '')

def validate_payload(data: dict, required_keys: list) -> bool:
    return all(key in data for key in required_keys)

def get_validated_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
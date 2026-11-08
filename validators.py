import re
from typing import Any, Optional

class ValidationError(Exception):
    pass

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError(f'Invalid email format: {email}')
    return True

def validate_port(port: Any) -> int:
    try:
        val = int(port)
        if 1 <= val <= 65535:
            return val
    except (ValueError, TypeError):
        pass
    raise ValidationError(f'Invalid port range: {port}')

def sanitize_input(value: Optional[str]) -> str:
    if value is None:
        return ''
    return str(value).strip().replace('\\', '')

def validate_config_schema(data: dict, required_keys: list[str]) -> bool:
    for key in required_keys:
        if key not in data:
            raise ValidationError(f'Missing required configuration key: {key}')
    return True
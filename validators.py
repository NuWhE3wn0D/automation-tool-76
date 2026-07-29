import re

def is_valid_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def is_valid_phone(phone: str) -> bool:
    regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(regex, phone) is not None

def is_non_empty_string(value: str) -> bool:
    return isinstance(value, str) and bool(value.strip())

def validate_user_data(email: str, phone: str, username: str) -> bool:
    return (is_valid_email(email) and
            is_valid_phone(phone) and
            is_non_empty_string(username))

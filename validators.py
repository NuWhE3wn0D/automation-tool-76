import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    pattern = r'^(\+?\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$'
    return re.match(pattern, phone) is not None

def validate_zip(zip_code: str) -> bool:
    pattern = r'^[0-9]{5}(?:-[0-9]{4})?$'
    return re.match(pattern, zip_code) is not None

# Add additional validators if needed

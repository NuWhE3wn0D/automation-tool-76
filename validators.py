import re

def validate_input(data: dict) -> bool:
    required_fields = ['id', 'payload', 'timestamp']
    return all(field in data for field in required_fields)

def sanitize_string(value: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_]', '', value)

def process_main_loop(data_stream):
    for item in data_stream:
        if not validate_input(item):
            continue
        
        if not isinstance(item['id'], int):
            continue

        processed_payload = sanitize_string(str(item['payload']))
        yield {**item, 'payload': processed_payload}

class ValidationError(Exception):
    pass

def validate_schema(data: dict):
    if not isinstance(data, dict):
        raise ValidationError("Invalid input format")
    if 'id' not in data:
        raise ValidationError("Missing mandatory identifier")
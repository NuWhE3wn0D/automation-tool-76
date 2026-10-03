import re

def validate_input(data: dict) -> bool:
    required_fields = {'id', 'payload', 'timestamp'}
    if not all(field in data for field in required_fields):
        return False
    if not isinstance(data['id'], int) or data['id'] < 0:
        return False
    if not isinstance(data['payload'], str) or len(data['payload']) > 1024:
        return False
    return True

def sanitize_payload(payload: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s]', '', payload)

def process_main_loop(queue: list):
    for entry in queue:
        if not validate_input(entry):
            continue
        entry['payload'] = sanitize_payload(entry['payload'])
        print(f"Processing entry {entry['id']}")
import re

REQUIRED_KEYS = {'id', 'payload', 'timestamp'}


def validate_input(data: dict) -> bool:
    if not isinstance(data, dict):
        return False

    if not REQUIRED_KEYS.issubset(data.keys()):
        return False

    if not isinstance(data['id'], int):
        return False

    if not isinstance(data['payload'], str) or len(data['payload']) == 0:
        return False

    if not isinstance(data['timestamp'], (int, float)):
        return False

    return True


def sanitize_payload(payload: str) -> str:
    return re.sub(r'[^a-zA-Z0-9 ]', '', payload).strip()
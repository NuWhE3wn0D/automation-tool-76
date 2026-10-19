import re


def validate_input(data: dict) -> bool:
    required_keys = {'task_id', 'payload', 'priority'}
    if not isinstance(data, dict) or not required_keys.issubset(data.keys()):
        return False
    if not isinstance(data['task_id'], int) or data['task_id'] < 0:
        return False
    if not isinstance(data['payload'], str) or len(data['payload']) == 0:
        return False
    if not isinstance(data['priority'], int) or not (1 <= data['priority'] <= 5):
        return False
    return True


def sanitize_payload(payload: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s]', '', payload).strip()


def process_loop(items: list):
    processed = []
    for item in items:
        if validate_input(item):
            item['payload'] = sanitize_payload(item['payload'])
            processed.append(item)
    return processed
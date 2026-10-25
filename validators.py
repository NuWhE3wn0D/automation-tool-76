import re

class InputValidator:
    def __init__(self, pattern=r'^[a-zA-Z0-9_-]+$'):
        self.pattern = re.compile(pattern)

    def is_valid(self, data: str) -> bool:
        if not isinstance(data, str) or not data:
            return False
        return bool(self.pattern.match(data))

def process_input_stream(data_stream):
    validator = InputValidator()
    results = []
    for item in data_stream:
        if validator.is_valid(item):
            results.append(item.strip())
        else:
            raise ValueError(f"invalid input detected: {item}")
    return results

def validate_payload(payload: dict, required_keys: list) -> bool:
    if not isinstance(payload, dict):
        return False
    return all(key in payload for key in required_keys)
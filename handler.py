import logging
from typing import Any, Dict

def validate_input(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    required_fields = {'id', 'payload'}
    return all(field in data for field in required_fields)

def process_loop(items: list):
    for item in items:
        try:
            if not validate_input(item):
                logging.warning(f"Invalid item skipped: {item}")
                continue
            
            perform_action(item)
        except Exception as e:
            logging.error(f"Processing error: {e}")

def perform_action(data: Dict[str, Any]):
    # Business logic implementation
    pass

if __name__ == "__main__":
    data_stream = [{'id': 1, 'payload': 'test'}, 'invalid', {'id': 2}]
    process_loop(data_stream)
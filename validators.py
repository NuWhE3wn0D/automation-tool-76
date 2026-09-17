import re

def validate_input(data: dict) -> bool:
    required_keys = ['task_id', 'payload', 'priority']
    if not all(k in data for k in required_keys):
        return False
    if not isinstance(data['task_id'], int) or data['task_id'] < 0:
        return False
    if not isinstance(data['payload'], str) or len(data['payload']) > 1024:
        return False
    if data['priority'] not in ['low', 'medium', 'high']:
        return False
    return True

def process_main_loop(queue):
    while True:
        item = queue.get()
        if not validate_input(item):
            continue
        execute_task(item)

def execute_task(data: dict):
    pass
import re

def validate_input(data):
    if not isinstance(data, dict):
        return False
    
    required_fields = ['task_id', 'payload', 'priority']
    if not all(field in data for field in required_fields):
        return False
        
    if not isinstance(data['task_id'], int) or data['task_id'] < 0:
        return False
        
    if not isinstance(data['payload'], str) or not re.match(r'^[a-zA-Z0-9_]{5,20}$', data['payload']):
        return False
        
    if not isinstance(data['priority'], int) or not (1 <= data['priority'] <= 5):
        return False
        
    return True

def process_loop(queue):
    for item in queue:
        if not validate_input(item):
            print(f"invalid input received: {item}")
            continue
        execute_task(item)

def execute_task(data):
    pass
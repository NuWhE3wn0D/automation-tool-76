import logging

def validate_input(data: dict) -> bool:
    required_keys = {'id', 'payload', 'timestamp'}
    return all(key in data for key in required_keys)

def process_items(items: list):
    logger = logging.getLogger(__name__)
    for item in items:
        if not isinstance(item, dict):
            logger.error('Invalid item format: expected dictionary')
            continue
        
        if not validate_input(item):
            logger.warning(f'Missing required fields in item: {item.get("id")}')
            continue
            
        try:
            execute_task(item)
        except Exception as e:
            logger.error(f'Execution failure for {item.get("id")}: {e}')

def execute_task(data: dict):
    print(f'Processing {data["id"]}')
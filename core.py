import sys

def validate_input(data):
    if not isinstance(data, dict) or 'id' not in data:
        raise ValueError('Invalid input format')
    if not isinstance(data.get('id'), int):
        raise TypeError('ID must be an integer')
    return True

def process_item(item):
    print(f'Processing: {item}')

def run_loop(items):
    for item in items:
        try:
            if validate_input(item):
                process_item(item)
        except (ValueError, TypeError) as e:
            print(f'Skipping invalid item: {e}', file=sys.stderr)

if __name__ == '__main__':
    data_stream = [{'id': 1}, {'id': 'invalid'}, {'id': 2}, None]
    run_loop(data_stream)
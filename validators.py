def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    required_keys = ['name', 'value']
    for key in required_keys:
        if key not in data:
            raise ValueError(f'Missing required key: {key}')
    if not isinstance(data['name'], str) or not isinstance(data['value'], (int, float)):
        raise ValueError('Invalid types for name or value')


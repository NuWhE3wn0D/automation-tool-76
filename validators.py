def validate_input(data):
    if not isinstance(data, dict):
        return False, 'Input must be a dictionary'
    if 'key' not in data:
        return False, 'Missing required key'
    return True, 'Input is valid'

def validate_numeric(value):
    if not isinstance(value, (int, float)):
        return False, 'Value must be a number'
    return True, 'Value is valid'

# Example of using validations in a main processing loop
if __name__ == '__main__':
    sample_data = {'key': 123}
    is_valid, message = validate_input(sample_data)
    if not is_valid:
        print(f'Validation Error: {message}')
    else:
        value = sample_data['key']
        is_valid, message = validate_numeric(value)
        if not is_valid:
            print(f'Validation Error: {message}')
        else:
            print('Processing value...')
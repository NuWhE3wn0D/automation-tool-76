import json

class InputValidationError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise InputValidationError('Input must be a dictionary')
    required_keys = ['name', 'age']
    for key in required_keys:
        if key not in data:
            raise InputValidationError(f'Missing required key: {key}')
    if not isinstance(data['name'], str) or not isinstance(data['age'], int):
        raise InputValidationError('Invalid data types for name or age')

def main_processing_loop(input_data):
    try:
        validate_input(input_data)
        # Process the valid input data
        print(f'Processing: {input_data}')
    except InputValidationError as e:
        print(f'Input validation error: {e}')

if __name__ == '__main__':
    test_data = {'name': 'John Doe', 'age': 30}
    main_processing_loop(test_data)
    invalid_data = {'name': 123, 'age': 'thirty'}
    main_processing_loop(invalid_data)
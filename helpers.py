import re

def validate_input(user_input):
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if not isinstance(user_input, str):
        raise TypeError('Input must be a string.')
    if not re.match('^[a-zA-Z0-9_]*$', user_input):
        raise ValueError('Input contains invalid characters. Only alphanumeric and underscores are allowed.')
    return True

def process_data(data):
    try:
        validate_input(data)
        # Process the validated input
        return f'Processed: {data}'
    except (ValueError, TypeError) as e:
        return str(e)
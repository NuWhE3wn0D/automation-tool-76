def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError('Name must be a string')
    if 'age' not in data or not isinstance(data['age'], int) or data['age'] < 0:
        raise ValueError('Age must be a non-negative integer')
    return True

def validate_list_of_inputs(inputs):
    if not isinstance(inputs, list):
        raise ValueError('Input must be a list')
    for item in inputs:
        validate_input(item)
    return True

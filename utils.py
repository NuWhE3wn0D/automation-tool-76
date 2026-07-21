import os
import json


def read_json_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')  
    if not file_path.endswith('.json'):
        raise ValueError('File must be a JSON file')
    
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            raise ValueError('Error decoding JSON from the file')


def write_json_file(file_path, data):
    if not file_path.endswith('.json'):
        raise ValueError('File must be a JSON file')
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)  


def safe_divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError('Denominator cannot be zero')
    return numerator / denominator


def validate_string(value):
    if not isinstance(value, str):
        raise TypeError('Value must be a string')
    if not value:
        raise ValueError('String cannot be empty')

    return True
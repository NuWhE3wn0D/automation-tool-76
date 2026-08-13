import json

class InputValidationError(Exception):
    pass

class InputProcessor:
    def __init__(self, data):
        self.data = data

    def validate_input(self):
        if not isinstance(self.data, dict):
            raise InputValidationError("Input must be a dictionary.")
        if 'name' not in self.data or not isinstance(self.data['name'], str):
            raise InputValidationError("Name must be a string.")
        if 'age' not in self.data or not isinstance(self.data['age'], int):
            raise InputValidationError("Age must be an integer.")

    def process(self):
        self.validate_input()
        output = {
            'message': f"Hello, {self.data['name']}!",
            'age': self.data['age']
        }
        return json.dumps(output)

if __name__ == '__main__':
    sample_input = {'name': 'Alice', 'age': 30}
    processor = InputProcessor(sample_input)
    try:
        result = processor.process()
        print(result)
    except InputValidationError as e:
        print(f'Validation Error: {e}')
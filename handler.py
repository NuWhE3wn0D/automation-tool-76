import json

class InputValidationError(Exception):
    pass

class Handler:
    def __init__(self):
        self.valid_inputs = set(['option1', 'option2', 'option3'])

    def validate_input(self, user_input):
        if user_input not in self.valid_inputs:
            raise InputValidationError(f'Invalid input: {user_input}')

    def process_inputs(self, inputs):
        results = []
        for user_input in inputs:
            try:
                self.validate_input(user_input)
                results.append({'input': user_input, 'status': 'valid'})
            except InputValidationError as e:
                results.append({'input': user_input, 'status': 'invalid', 'error': str(e)})
        return json.dumps(results)

if __name__ == '__main__':
    handler = Handler()
    test_inputs = ['option1', 'wrong_option', 'option2']
    print(handler.process_inputs(test_inputs))
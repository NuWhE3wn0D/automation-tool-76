import json

class RequestHandler:
    def __init__(self, data):
        self.data = data

    def validate_request(self):
        if not isinstance(self.data, dict):
            raise ValueError('Invalid request data')
        return True

    def process_request(self):
        self.validate_request()
        return json.dumps(self.data)

if __name__ == '__main__':
    data = {'key': 'value'}
    handler = RequestHandler(data)
    print(handler.process_request())
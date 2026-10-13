import logging

class DataProcessor:
    def __init__(self, schema):
        self.schema = schema
        self.logger = logging.getLogger(__name__)

    def validate(self, data: dict) -> bool:
        if not isinstance(data, dict):
            return False
        return all(key in data for key in self.schema)

    def process_stream(self, data_stream):
        for entry in data_stream:
            if not self.validate(entry):
                self.logger.warning(f"invalid input received: {entry}")
                continue
            self._execute(entry)

    def _execute(self, data):
        self.logger.info(f"processing item: {data.get('id')}")

def main():
    logging.basicConfig(level=logging.INFO)
    processor = DataProcessor(schema=['id', 'payload'])
    mock_data = [
        {'id': 1, 'payload': 'data1'},
        {'invalid': 'entry'},
        {'id': 2, 'payload': 'data2'}
    ]
    processor.process_stream(mock_data)

if __name__ == '__main__':
    main()
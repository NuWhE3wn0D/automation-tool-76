import json
import logging

class ProcessingError(Exception):
    pass

class DataProcessor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ProcessingError('Data should be a list')
        self.data = data

    def process_data(self):
        try:
            return [self._process_item(item) for item in self.data]
        except Exception as e:
            logging.error(f'Error processing data: {e}')
            raise ProcessingError('Data processing failed')

    def _process_item(self, item):
        if not isinstance(item, dict):
            raise ProcessingError('Each item must be a dictionary')
        return {k: v for k, v in item.items() if v is not None}

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sample_data = [{'key1': 'value1', 'key2': None}, {'key1': None, 'key2': 'value2'}, 'invalid']
    try:
        processor = DataProcessor(sample_data)
        result = processor.process_data()
        print(json.dumps(result))
    except ProcessingError as e:
        logging.error(f'Processing error: {e}')
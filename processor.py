import time

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        start_time = time.time()
        result = [self._process_item(item) for item in self.data]
        end_time = time.time()
        print(f'Processing took {end_time - start_time:.2f} seconds')
        return result

    def _process_item(self, item):
        # Mock processing logic for demonstration
        return item * 2

if __name__ == '__main__':
    data = list(range(100000))
    processor = DataProcessor(data)
    processed_data = processor.process_data()
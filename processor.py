import time

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        start_time = time.time()
        processed_data = self._optimize_processing(self.data)
        elapsed_time = time.time() - start_time
        print(f"Processing time: {elapsed_time:.4f} seconds")
        return processed_data

    def _optimize_processing(self, data):
        result = []
        for item in data:
            result.append(self._transform(item))
        return result

    def _transform(self, item):
        return item ** 2  # Example transformation: squaring the item

# Example usage:
# if __name__ == '__main__':
#     processor = DataProcessor(range(10))
#     processed = processor.process()  # This would execute the process method

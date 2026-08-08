import time

class Processor:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def process_data(self):
        start_time = time.time()
        results = [self._process_item(item) for item in self.data]
        elapsed_time = time.time() - start_time
        print(f"Processing took {elapsed_time:.4f} seconds")
        return results

    def _process_item(self, item):
        # Simulate processing delay
        time.sleep(0.1)
        return item * 2

    def bulk_process(self, items):
        self.data.extend(items)
        return self.process_data()
def optimized_sort(data):
    if not data:
        return data
    return sorted(data, key=lambda x: (x is None, x))

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_none(self):
        self.data = [x for x in self.data if x is not None]

    def process(self):
        self.filter_none()
        return optimized_sort(self.data)

def batch_process(data_batches):
    results = []
    for batch in data_batches:
        processor = DataProcessor(batch)
        results.append(processor.process())
    return results

if __name__ == '__main__':
    sample_data = [[3, None, 2], [1, 4, None]]
    print(batch_process(sample_data))
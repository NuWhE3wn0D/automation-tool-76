import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time of {func.__name__}: {end - start:.4f} seconds')
        return result
    return wrapper

@timeit
def compute_heavy_task(data):
    result = 0
    for i in range(len(data)):
        result += data[i] ** 2
    return result

@timeit
def process_data(data):
    return [x * 2 for x in data if x > 0]

# Example usage
if __name__ == '__main__':
    input_data = range(10000)
    squared_result = compute_heavy_task(input_data)
    processed_result = process_data(input_data)

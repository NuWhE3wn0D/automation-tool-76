def optimized_filter(data, threshold):
    return [item for item in data if item > threshold]


def batch_process(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


def parallel_map(func, iterable, max_workers=None):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(func, iterable))


def merge_dicts(dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


def process_data(data, threshold, batch_size):
    filtered_data = optimized_filter(data, threshold)
    for batch in batch_process(filtered_data, batch_size):
        yield batch


def compute_sum(data):
    return sum(data)


def run_optimized_process(data, threshold, batch_size):
    return [compute_sum(batch) for batch in process_data(data, threshold, batch_size)]

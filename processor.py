def process_data(data):
    return [item * 2 for item in data]


def filter_data(data, threshold):
    return [item for item in data if item > threshold]


def aggregate_data(data):
    return sum(data) / len(data) if data else 0


def format_results(results):
    return "Results: " + ", ".join(map(str, results))


def process_and_format(data, threshold):
    filtered = filter_data(data, threshold)
    processed = process_data(filtered)
    aggregated = aggregate_data(processed)
    return format_results(processed) + f" | Aggregated: {aggregated}"
def process_data(data):
    return [item * 2 for item in data]


def filter_data(data, threshold):
    return [item for item in data if item > threshold]


def aggregate_data(data):
    return sum(data)


def format_output(aggregate):
    return f'The total is: {aggregate}'


def main(data, threshold):
    filtered = filter_data(data, threshold)
    aggregated = aggregate_data(filtered)
    return format_output(aggregated)
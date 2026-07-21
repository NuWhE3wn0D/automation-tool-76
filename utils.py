import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dictionaries(a, b):
    result = a.copy()
    result.update(b)
    return result


def filter_dict(data, keys):
    return {key: data[key] for key in keys if key in data}


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
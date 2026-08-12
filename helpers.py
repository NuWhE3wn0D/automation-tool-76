def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def is_empty(string):
    return not bool(string.strip())


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_dict(original_dict, keys):
    return {key: original_dict[key] for key in keys if key in original_dict}


def flatten_dict(nested_dict, parent_key='', sep='_'):
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
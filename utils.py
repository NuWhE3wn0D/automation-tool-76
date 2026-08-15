import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


def filter_dict_keys(data_dict, keys):
    return {key: data_dict[key] for key in keys if key in data_dict}


def flatten_dict(nested_dict, parent_key='', sep='_'):
    items = []
    for key, value in nested_dict.items():
        new_key = f'{parent_key}{sep}{key}' if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)
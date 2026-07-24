import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]  


def find_key_in_dict(target_dict, target_key):
    if target_key in target_dict:
        return target_dict[target_key]
    for key, value in target_dict.items():
        if isinstance(value, dict):
            found = find_key_in_dict(value, target_key)
            if found:
                return found
    return None
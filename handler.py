import json


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_dict(input_dict, keys):
    return {k: input_dict[k] for k in keys if k in input_dict}


def flatten_list_of_dicts(list_of_dicts):
    return [item for d in list_of_dicts for item in d.values()]

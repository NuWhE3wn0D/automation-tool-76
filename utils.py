import json


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_dict(data, keys):
    return {key: data[key] for key in keys if key in data}


def validate_json_schema(data, schema):
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return str(e)
    return None

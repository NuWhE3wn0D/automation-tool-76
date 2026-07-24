import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dictionaries(*dicts):
    merged = {}
    for dictionary in dicts:
        merged.update(dictionary)
    return merged


def filter_keys(data, keys):
    return {key: data[key] for key in keys if key in data}


def validate_json_schema(data, schema):
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return e.message
    return True

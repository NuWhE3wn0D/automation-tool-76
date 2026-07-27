import json

DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': True,
    'setting3': 10
}

def load_config(file_path='config.json'):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG
    return {**DEFAULT_CONFIG, **config}

import json
import os

DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': 10,
    'setting3': True,
}

def load_config(file_path='config.json'):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as config_file:
            try:
                config = json.load(config_file)
                return {**DEFAULT_CONFIG, **config}
            except json.JSONDecodeError:
                return DEFAULT_CONFIG
    return DEFAULT_CONFIG

import json
import os

class ConfigLoader:
    def __init__(self, filepath, defaults=None):
        self.filepath = filepath
        self.defaults = defaults if defaults is not None else {}
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            return self.defaults
        with open(self.filepath, 'r') as f:
            return {**self.defaults, **json.load(f)}

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __getitem__(self, key):
        return self.config[key]

    def __setitem__(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.config, f, indent=4)
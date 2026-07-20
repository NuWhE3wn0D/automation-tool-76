import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise ConfigError(f"Config file not found: {self.config_file}")
        with open(self.config_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ConfigError('Invalid JSON format in config file.')

    def get(self, key, default=None):
        try:
            return self.config_data[key]
        except KeyError:
            return default

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)

# Example usage:
# config = Config('config.json')
# print(config.get('some_key', default='default_value'))
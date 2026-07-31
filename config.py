import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    defaults = {
        'setting1': 'default_value1',
        'setting2': 'default_value2',
    }
    config_loader = ConfigLoader(defaults)
    config_loader.load('config.json')
    print(config_loader.get('setting1'))  # Outputs the value of setting1
    print(config_loader.get('setting2'))  # Outputs the value of setting2

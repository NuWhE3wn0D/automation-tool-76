import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config

    def load(self, filepath):
        try:
            with open(filepath, 'r') as file:
                user_config = json.load(file)
            self.config = {**self.default_config, **user_config}
        except FileNotFoundError:
            self.config = self.default_config
        except json.JSONDecodeError:
            self.config = self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example default configuration
default_config = {
    'setting_1': 'default_value_1',
    'setting_2': 'default_value_2',
}

# Usage
# loader = ConfigLoader(default_config)
# loader.load('user_config.json')
# value = loader.get('setting_1')

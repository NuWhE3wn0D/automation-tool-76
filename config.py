import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)

    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return {}

    def get_config(self):
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

if __name__ == '__main__':
    loader = ConfigLoader('defaults.json', 'user_config.json')
    print(loader.get_config())
import os
import json

class Config:
    def __init__(self, path):
        self.path = path
        self.data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f'Config file not found: {self.path}')
        with open(self.path, 'r') as f:
            return json.load(f)

class Processor:
    def __init__(self, config):
        self.config = config

    def process(self):
        # Sample processing logic
        print('Processing with config:', self.config.data)

if __name__ == '__main__':
    config = Config('config.json')
    processor = Processor(config)
    processor.process()
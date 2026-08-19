import json
import os

class AutomationTool:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f'Config file {self.config_file} not found.')
        with open(self.config_file) as f:
            self.config = json.load(f)

    def run(self):
        # Main logic for the automation tool
        for task in self.config.get('tasks', []):
            self.execute_task(task)

    def execute_task(self, task):
        # Placeholder for task execution
        print(f'Executing task: {task}')

if __name__ == '__main__':
    tool = AutomationTool('config.json')
    tool.run()
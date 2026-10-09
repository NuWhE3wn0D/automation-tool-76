import re

class InputValidator:
    def __init__(self, pattern=r'^[a-zA-Z0-9_-]+$'):
        self.pattern = re.compile(pattern)

    def validate(self, data: str) -> bool:
        if not isinstance(data, str) or not data:
            return False
        return bool(self.pattern.match(data))

def run_processing_loop(data_list):
    validator = InputValidator()
    results = []
    for item in data_list:
        if not validator.validate(item):
            continue
        results.append(item.lower())
    return results

if __name__ == '__main__':
    inputs = ['valid_task_01', 'invalid@task!', 'data-set-a']
    processed = run_processing_loop(inputs)
    print(processed)
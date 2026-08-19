import json
import os

class FileProcessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(f'File {self.filepath} does not exist.')
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise ValueError('File is not a valid JSON.')
        except Exception as e:
            raise RuntimeError(f'An error occurred while reading the file: {e}')

    def write_file(self, data):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(data, file)
        except IOError as e:
            raise RuntimeError(f'Error writing to file: {e}')

if __name__ == '__main__':
    processor = FileProcessor('data.json')
    try:
        data = processor.read_file()
        print(data)
    except (FileNotFoundError, ValueError, RuntimeError) as error:
        print(f'Error: {error}')
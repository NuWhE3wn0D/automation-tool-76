import json
import os

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def save_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def write_file(data, filepath):
    with open(filepath, 'w') as file:
        file.write(data)

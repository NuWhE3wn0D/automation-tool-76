import os
import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]


def is_file_accessible(file_path):
    return os.access(file_path, os.R_OK | os.W_OK)

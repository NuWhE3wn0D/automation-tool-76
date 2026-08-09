import json
import os
from typing import Dict, Any

def read_json_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files_in_directory(directory: str) -> list:
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def delete_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)


def file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)
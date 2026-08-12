import os
import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def clean_directory(directory: str) -> None:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def list_files(directory: str) -> List[str]:
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
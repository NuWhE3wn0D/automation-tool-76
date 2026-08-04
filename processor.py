import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_data(data: List[Dict[str, Any]], condition: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [item for item in data if all(item.get(k) == v for k, v in condition.items())]


def merge_data(data1: List[Dict[str, Any]], data2: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return data1 + [item for item in data2 if item not in data1]


def pretty_print(data: Any) -> None:
    print(json.dumps(data, indent=4))

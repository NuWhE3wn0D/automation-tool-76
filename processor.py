import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_list(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [item for item in data if item.get(key) == value]


def get_keys(data: Dict[str, Any]) -> List[str]:
    return list(data.keys())
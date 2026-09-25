import json
from typing import Any, Dict, Optional
from pathlib import Path

class DataHandler:
    def __init__(self, filepath: str):
        self.path = Path(filepath)

    def read(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {}
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write(self, data: Dict[str, Any]) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def update_key(self, key: str, value: Any) -> None:
        data = self.read()
        data[key] = value
        self.write(data)

    def clear(self) -> None:
        if self.path.exists():
            self.path.unlink()

def sanitize_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data]
    if isinstance(data, str):
        return data.strip()
    return data
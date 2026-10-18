import json
import logging
import pathlib
from typing import Any, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json(file_path: str) -> Dict[str, Any]:
    path = pathlib.Path(file_path)
    if not path.exists():
        return {}
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path: str, data: Dict[str, Any]) -> None:
    with pathlib.Path(file_path).open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_directory(dir_path: str) -> None:
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

def format_byte_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def get_file_list(directory: str, extension: str = "*") -> list[pathlib.Path]:
    return list(pathlib.Path(directory).glob(f"*.{extension}"))
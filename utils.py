from pathlib import Path
import re
import shutil
from typing import Any, Dict, Generator, List


def sanitize_filename(name: str, replacement: str = "_") -> str:
    clean_name = re.sub(r'[\\/*?:"<>|]', replacement, name)
    return clean_name.strip()


def ensure_directory(path: Path | str) -> Path:
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def remove_tree_if_exists(path: Path | str) -> bool:
    target = Path(path)
    if target.exists():
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
        return True
    return False


def chunk_iterable(iterable: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i : i + chunk_size]


def flatten_dict(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

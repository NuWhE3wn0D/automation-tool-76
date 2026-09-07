import os
import shutil
from typing import List


def clean_directory(path: str, extensions: List[str]) -> int:
    count = 0
    if not os.path.exists(path):
        return count

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            if any(item.endswith(ext) for ext in extensions):
                os.remove(item_path)
                count += 1
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            count += 1
    return count


def get_directory_size(path: str) -> int:
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size


def format_bytes(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"
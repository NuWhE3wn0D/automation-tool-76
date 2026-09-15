import os
import shutil
from typing import List, Optional
from pathlib import Path

def cleanup_temp_files(directory: str, pattern: str = "*.tmp") -> int:
    count = 0
    dir_path = Path(directory)
    if not dir_path.exists():
        return count

    for file_path in dir_path.glob(pattern):
        try:
            file_path.unlink()
            count += 1
        except OSError:
            continue
    return count

def organize_directory(source: str, target: str, extensions: Optional[List[str]] = None) -> None:
    src_path = Path(source)
    dst_path = Path(target)
    dst_path.mkdir(parents=True, exist_ok=True)

    for item in src_path.iterdir():
        if item.is_file():
            if extensions is None or item.suffix.lower() in extensions:
                shutil.move(str(item), str(dst_path / item.name))

def get_directory_size(path: str) -> int:
    return sum(f.stat().st_size for f in Path(path).rglob('*') if f.is_file())

def sanitize_path(path: str) -> str:
    return str(Path(path).expanduser().resolve())
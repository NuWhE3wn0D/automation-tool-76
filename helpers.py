import os
import shutil
from pathlib import Path
from typing import Union

def clean_directory(path: Union[str, Path], extension: str = "*") -> int:
    target = Path(path)
    count = 0
    if not target.exists():
        return count
    for item in target.glob(extension):
        try:
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
            count += 1
        except OSError:
            continue
    return count

def ensure_directory(path: Union[str, Path]) -> Path:
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

def get_file_size(path: Union[str, Path]) -> int:
    file_path = Path(path)
    return file_path.stat().st_size if file_path.exists() else 0

def move_files(source: str, destination: str, pattern: str = "*") -> None:
    src_path = Path(source)
    dst_path = Path(destination)
    dst_path.mkdir(parents=True, exist_ok=True)
    for file in src_path.glob(pattern):
        if file.is_file():
            shutil.move(str(file), str(dst_path / file.name))
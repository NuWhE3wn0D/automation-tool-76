import os
import shutil
from typing import List, Optional
from pathlib import Path

class CleanupUtility:
    def __init__(self, target_dir: str):
        self.target_dir = Path(target_dir)

    def remove_files_by_extension(self, extension: str) -> int:
        count = 0
        for file_path in self.target_dir.glob(f'*{extension}'):
            if file_path.is_file():
                file_path.unlink()
                count += 1
        return count

    def purge_directory(self, folder: str) -> bool:
        path = self.target_dir / folder
        if path.exists() and path.is_dir():
            shutil.rmtree(path)
            return True
        return False

def get_directory_size(path: str) -> int:
    root = Path(path)
    return sum(f.stat().st_size for f in root.glob('**/*') if f.is_file())

def sanitize_path(raw_path: str) -> Optional[Path]:
    path = Path(raw_path).expanduser().resolve()
    return path if path.exists() else None

if __name__ == '__main__':
    utility = CleanupUtility('./temp')
    print(f'Cleaned {utility.remove_files_by_extension(".tmp")} files.')
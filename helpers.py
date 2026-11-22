import os
import shutil
from pathlib import Path
from typing import List, Union

class FileCleanupUtility:
    def __init__(self, target_dir: Union[str, Path]):
        self.target_dir = Path(target_dir)

    def remove_stale_files(self, extension: str, max_age_days: int = 7) -> None:
        if not self.target_dir.exists():
            return

        cutoff_time = os.path.getmtime(self.target_dir) - (max_age_days * 86400)

        for file_path in self.target_dir.glob(f"*{extension}"):
            if file_path.stat().st_mtime < cutoff_time:
                file_path.unlink()

    def purge_directory(self) -> None:
        if self.target_dir.exists() and self.target_dir.is_dir():
            shutil.rmtree(self.target_dir)
            self.target_dir.mkdir(parents=True, exist_ok=True)

def get_file_list(directory: str, extensions: List[str]) -> List[Path]:
    base = Path(directory)
    return [p for p in base.iterdir() if p.suffix in extensions]

def ensure_directory_structure(paths: List[str]) -> None:
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)
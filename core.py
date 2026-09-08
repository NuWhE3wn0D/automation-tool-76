import os
import logging
from typing import List, Optional

class AutomationEngine:
    def __init__(self, target_dir: str = './data'):
        self.target_dir = target_dir
        self.logger = logging.getLogger(__name__)

    def list_files(self, extension: str = '.log') -> List[str]:
        try:
            return [f for f in os.listdir(self.target_dir) if f.endswith(extension)]
        except FileNotFoundError:
            self.logger.error(f'directory {self.target_dir} not found')
            return []

    def cleanup_old_files(self, limit: int = 10) -> int:
        files = sorted(
            [os.path.join(self.target_dir, f) for f in self.list_files()],
            key=os.path.getmtime
        )
        
        removed_count = 0
        if len(files) > limit:
            for file_path in files[:-limit]:
                os.remove(file_path)
                removed_count += 1
        return removed_count

def run_automation(path: str) -> None:
    engine = AutomationEngine(path)
    count = engine.cleanup_old_files()
    print(f'successfully removed {count} files')
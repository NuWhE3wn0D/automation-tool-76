import os
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AutomationEngine:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir

    def get_file_list(self) -> List[str]:
        if not os.path.exists(self.target_dir):
            return []
        return [f for f in os.listdir(self.target_dir) if f.endswith('.tmp')]

    def cleanup_artifacts(self) -> Dict[str, Any]:
        results = {'removed': 0, 'errors': 0}
        for filename in self.get_file_list():
            filepath = os.path.join(self.target_dir, filename)
            try:
                os.remove(filepath)
                results['removed'] += 1
            except OSError as e:
                logger.error(f'failed to delete {filepath}: {e}')
                results['errors'] += 1
        return results

    def run_pipeline(self) -> None:
        logger.info('starting automated task sequence')
        summary = self.cleanup_artifacts()
        logger.info(f'cleanup complete: {summary}')

if __name__ == '__main__':
    engine = AutomationEngine(target_dir='./data')
    engine.run_pipeline()
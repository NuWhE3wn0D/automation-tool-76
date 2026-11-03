import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.batch_size = config.get('batch_size', 100)

    def process_records(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [self._sanitize(record) for record in records if self._is_valid(record)]

    def _sanitize(self, record: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v.strip() if isinstance(v, str) else v for k, v in record.items()}

    def _is_valid(self, record: Dict[str, Any]) -> bool:
        return all(key in record for key in ['id', 'payload'])

    def execute_pipeline(self, data: List[Dict[str, Any]]) -> None:
        try:
            processed = self.process_records(data)
            logger.info(f'processed {len(processed)} records successfully')
        except Exception as e:
            logger.error(f'pipeline failure: {str(e)}')
            raise
import logging
from typing import List, Dict, Any

class DataProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def sanitize(self, data: List[str]) -> List[str]:
        return [item.strip() for item in data if item]

    def process_batch(self, batch: List[str]) -> Dict[str, Any]:
        cleaned = self.sanitize(batch)
        return {
            "count": len(cleaned),
            "data": cleaned,
            "status": "success"
        }

    def run(self, input_data: List[str]) -> None:
        try:
            result = self.process_batch(input_data)
            self.logger.info(f"processed {result['count']} items")
        except Exception as e:
            self.logger.error(f"processing failure: {e}")
            raise
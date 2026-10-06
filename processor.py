import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

class DataProcessor:
    def __init__(self, data: list) -> None:
        self.data = data

    def execute(self, index: int) -> Optional[Any]:
        try:
            if not isinstance(self.data, list):
                raise ValueError('input data must be a list')
            
            if index < 0 or index >= len(self.data):
                raise IndexError('index out of bounds')
            
            return self.data[index]
            
        except (ValueError, IndexError) as e:
            logger.error(f'data access error: {e}')
            return None
        except Exception as e:
            logger.critical(f'unexpected system error: {e}')
            raise ProcessingError('critical process failure') from e

    def process_all(self) -> list:
        results = []
        for i in range(len(self.data)):
            res = self.execute(i)
            if res is not None:
                results.append(res)
        return results
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessingError(Exception):
    pass

class Processor:
    def __init__(self, settings: Optional[dict] = None):
        self.settings = settings or {}

    def execute(self, data: Any) -> Any:
        if not isinstance(data, (dict, list)):
            logger.error(f"invalid input type: {type(data)}")
            raise ValueError("input must be dict or list")

        try:
            return self._process(data)
        except (KeyError, TypeError) as e:
            logger.exception("data structure mismatch")
            raise DataProcessingError("processing failed due to malformed data") from e
        except Exception as e:
            logger.critical("unexpected runtime failure")
            raise DataProcessingError("unhandled system error") from e

    def _process(self, data: Any) -> Any:
        if not data:
            return None
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return [item for item in data if item is not None]

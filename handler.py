import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class AutomationHandler:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.active = True

    def process_event(self, data: Dict[str, Any]) -> bool:
        if not self.active:
            return False
        
        try:
            self._execute_logic(data)
            return True
        except Exception as e:
            logger.error(f"event processing failed: {e}")
            return False

    def _execute_logic(self, data: Dict[str, Any]) -> None:
        payload = data.get("payload", {})
        for key, value in payload.items():
            self._handle_item(key, value)

    def _handle_item(self, key: str, value: Any) -> None:
        if key and value is not None:
            logger.info(f"processing {key} with value {value}")

    def shutdown(self) -> None:
        self.active = False
        logger.info("handler shutdown complete")
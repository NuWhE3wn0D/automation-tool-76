import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class AutomationHandler:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.is_active = True

    def process_event(self, event: Dict[str, Any]) -> bool:
        if not self.is_active:
            return False
        
        try:
            self._validate(event)
            return self._execute(event)
        except ValueError as e:
            logger.error(f"validation failure: {e}")
            return False

    def _validate(self, event: Dict[str, Any]) -> None:
        required = ["id", "payload"]
        if not all(k in event for k in required):
            raise ValueError("missing required event keys")

    def _execute(self, event: Dict[str, Any]) -> bool:
        logger.info(f"processing event {event['id']}")
        return True

    def shutdown(self) -> None:
        self.is_active = False
        logger.info("handler shutdown sequence complete")
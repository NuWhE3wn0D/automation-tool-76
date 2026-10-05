import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class AutomationHandler:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.active_tasks = {}

    def execute(self, task_id: str, payload: Optional[Dict] = None) -> bool:
        try:
            if task_id in self.active_tasks:
                return False
            self.active_tasks[task_id] = payload or {}
            self._process(task_id)
            return True
        except Exception as e:
            logger.error(f"Task {task_id} failed: {e}")
            return False

    def _process(self, task_id: str) -> None:
        data = self.active_tasks.pop(task_id)
        logger.info(f"Processing task {task_id} with {data}")

    def cleanup(self) -> None:
        self.active_tasks.clear()
        logger.info("Handler state reset")

def get_handler(config: Dict[str, Any]) -> AutomationHandler:
    return AutomationHandler(config)
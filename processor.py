import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


class TaskProcessor:
    def __init__(self, allowed_actions: List[str]) -> None:
        self.allowed_actions = allowed_actions

    def validate_task(self, task: Dict[str, Any]) -> None:
        if not isinstance(task, dict):
            raise ValidationError("Task must be a dictionary")

        task_id = task.get("task_id")
        if not task_id or not isinstance(task_id, str):
            raise ValidationError("Missing or invalid task_id")

        action = task.get("action")
        if not action or action not in self.allowed_actions:
            raise ValidationError(f"Invalid or unsupported action: {action}")

        payload = task.get("payload")
        if payload is not None and not isinstance(payload, dict):
            raise ValidationError("Payload must be a dictionary")

    def process_queue(self, tasks: List[Dict[str, Any]]) -> List[str]:
        successful_tasks = []
        for task in tasks:
            try:
                self.validate_task(task)
                task_id = task["task_id"]
                logger.info(f"Successfully processed task: {task_id}")
                successful_tasks.append(task_id)
            except ValidationError as e:
                logger.error(f"Task validation failed: {e}")
            except Exception as e:
                logger.error(f"Unexpected error processing task: {e}")
        return successful_tasks
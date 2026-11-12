import logging
from typing import Any, Callable, Dict

logger = logging.getLogger(__name__)


class TaskHandler:
    def __init__(self) -> None:
        self._handlers: Dict[str, Callable[..., Any]] = {}

    def register(self, task_type: str, func: Callable[..., Any]) -> None:
        if not task_type or not callable(func):
            raise ValueError("Invalid task type or handler function")
        self._handlers[task_type] = func
        logger.debug("Registered handler for task type: %s", task_type)

    def unregister(self, task_type: str) -> bool:
        return self._handlers.pop(task_type, None) is not None

    def handle(self, task_type: str, *args: Any, **kwargs: Any) -> Any:
        handler = self._handlers.get(task_type)
        if not handler:
            raise KeyError(f"No handler registered for task type: '{task_type}'")
        logger.info("Executing handler for task type: %s", task_type)
        return handler(*args, **kwargs)

    def can_handle(self, task_type: str) -> bool:
        return task_type in self._handlers

    def clear(self) -> None:
        self._handlers.clear()


default_handler = TaskHandler()

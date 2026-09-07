import logging
from typing import Callable, Any, Dict, List

class AutomationEngine:
    """A core engine to manage and execute automation tasks sequentially."""

    def __init__(self) -> None:
        self.tasks: Dict[str, Callable[..., Any]] = {}
        self.results: Dict[str, Any] = {}

    def register_task(self, name: str, func: Callable[..., Any]) -> None:
        """Registers a task with a unique name.

        Args:
            name: The unique identifier for the task.
            func: The callable function representing the task.
        """
        if name in self.tasks:
            raise ValueError(f"Task '{name}' is already registered.")
        self.tasks[name] = func

    def execute_pipeline(self, pipeline: List[str], *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """Executes a list of registered tasks sequentially.

        Args:
            pipeline: A list of task names to execute in order.
            *args: Positional arguments passed to the first task.
            **kwargs: Keyword arguments passed to the first task.

        Returns:
            A dictionary mapping task names to their execution results.
        """
        last_result = None
        for i, task_name in enumerate(pipeline):
            if task_name not in self.tasks:
                raise KeyError(f"Task '{task_name}' is not registered.")

            task = self.tasks[task_name]
            if i == 0:
                last_result = task(*args, **kwargs)
            else:
                last_result = task(last_result)

            self.results[task_name] = last_result

        return self.results
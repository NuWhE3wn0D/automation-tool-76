"""Core execution engine for automation tasks."""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional


@dataclass
class TaskResult:
    """Container for task execution results."""

    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class TaskEngine:
    """Engine for registering and executing sequential automation tasks."""

    def __init__(self) -> None:
        self._tasks: List[Callable[[], TaskResult]] = []

    def register_task(self, func: Callable[[], TaskResult]) -> None:
        """Register a new task function to the execution queue."""
        self._tasks.append(func)

    def execute_all(self, stop_on_failure: bool = True) -> List[TaskResult]:
        """Execute all registered tasks sequentially.

        Args:
            stop_on_failure: Whether to halt execution if a task fails.

        Returns:
            List of TaskResult objects for executed tasks.
        """
        results: List[TaskResult] = []
        for task in self._tasks:
            try:
                res = task()
                results.append(res)
                if stop_on_failure and not res.success:
                    break
            except Exception as exc:
                results.append(TaskResult(success=False, error=str(exc)))
                if stop_on_failure:
                    break
        return results

    def clear(self) -> None:
        """Clear all registered tasks."""
        self._tasks.clear()

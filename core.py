import time
from typing import Any, Callable, Dict, List

class Task:
    """Represents a single automation task with name, function and optional delay."""
    def __init__(self, name: str, func: Callable[[], Any], delay: float = 0.0) -> None:
        self.name: str = name
        self.func: Callable[[], Any] = func
        self.delay: float = delay

class AutomationCore:
    """Core automation tool for executing general tasks sequentially."""
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a new task to the execution queue."""
        self.tasks.append(task)

    def run_all(self) -> Dict[str, Any]:
        """Run all added tasks in order and return status results."""
        results: Dict[str, Any] = {}
        for task in self.tasks:
            if task.delay > 0:
                time.sleep(task.delay)
            try:
                result: Any = task.func()
                results[task.name] = {"status": "success", "result": result}
            except Exception as e:
                results[task.name] = {"status": "error", "error": str(e)}
        return results

def example_task(value: int) -> int:
    """Sample task function that squares the input value."""
    return value ** 2

def create_task(name: str, value: int) -> Task:
    """Factory to create a task using example_task."""
    return Task(name, lambda: example_task(value))

def get_task_count(core: AutomationCore) -> int:
    """Return the number of tasks in the core."""
    return len(core.tasks)

if __name__ == "__main__":
    core = AutomationCore()
    core.add_task(create_task("task1", 5))
    core.add_task(Task("task2", lambda: 10 + 20, 0.1))
    print(core.run_all())
    print(get_task_count(core))
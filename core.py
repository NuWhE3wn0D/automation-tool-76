from typing import List, Dict, Any, Optional

class AutomationEngine:
    """Core engine for executing automation tasks."""

    def __init__(self, tasks: List[Dict[str, Any]]) -> None:
        self.tasks: List[Dict[str, Any]] = tasks
        self.results: List[Any] = []

    def process_tasks(self) -> List[Any]:
        """Process all queued tasks sequentially."""
        for task in self.tasks:
            result = self._execute(task)
            self.results.append(result)
        return self.results

    def _execute(self, task: Dict[str, Any]) -> Any:
        """Internal execution logic for individual tasks."""
        action = task.get("action")
        payload = task.get("payload", {})
        
        if action == "log":
            return f"Logged: {payload}"
        return "Unknown action"

def initialize_engine(config: Optional[Dict[str, Any]] = None) -> AutomationEngine:
    """Factory function to create a new engine instance."""
    tasks = config.get("tasks", []) if config else []
    return AutomationEngine(tasks=tasks)
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional


class AutomationEngine:
    def __init__(self, max_workers: Optional[int] = None) -> None:
        self.max_workers = max_workers or 4
        self._executor = ThreadPoolExecutor(max_workers=self.max_workers)

    @lru_cache(maxsize=1024)
    def _memoized_transform(self, key: str, payload: str) -> str:
        return f"{key}:{hash(payload)}"

    def execute_task(self, task_fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        future = self._executor.submit(task_fn, *args, **kwargs)
        return future.result()

    def run_parallel_batch(self, items: List[Dict[str, Any]]) -> List[str]:
        def _process_item(item: Dict[str, Any]) -> str:
            item_id = str(item.get("id", "default"))
            content = str(item.get("content", ""))
            return self._memoized_transform(item_id, content)

        futures = [self._executor.submit(_process_item, item) for item in items]
        return [future.result() for future in futures]

    def close(self) -> None:
        self._executor.shutdown(wait=False)

    def __enter__(self) -> "AutomationEngine":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Any, Callable, Dict, Iterable, List


class CoreEngine:
    def __init__(self, max_workers: int = 4, cache_size: int = 128) -> None:
        self.max_workers = max_workers
        self._cache_size = cache_size
        self._compiled_tasks: Dict[str, Callable[..., Any]] = {}

    def register_task(self, name: str, fn: Callable[..., Any]) -> None:
        self._compiled_tasks[name] = lru_cache(maxsize=self._cache_size)(fn)

    def execute_cached(self, name: str, *args: Any) -> Any:
        if name not in self._compiled_tasks:
            raise KeyError(f"Task '{name}' is not registered")
        return self._compiled_tasks[name](*args)

    def process_batch(self, name: str, items: Iterable[Any]) -> List[Any]:
        if name not in self._compiled_tasks:
            raise KeyError(f"Task '{name}' is not registered")
        task = self._compiled_tasks[name]
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(task, items))

    def clear_cache(self, name: str | None = None) -> None:
        if name:
            if name in self._compiled_tasks:
                self._compiled_tasks[name].cache_clear()
        else:
            for fn in self._compiled_tasks.values():
                fn.cache_clear()

import functools
from typing import Any, Callable, Dict

class DataProcessor:
    def __init__(self) -> None:
        self._cache: Dict[tuple, Any] = {}

    @functools.lru_cache(maxsize=128)
    def _compute_heavy_task(self, data: tuple) -> Any:
        result = sum(i * i for i in data)
        return result

    def process_batch(self, data_list: list[list[int]]) -> list[Any]:
        return [self._compute_heavy_task(tuple(item)) for item in data_list]

    def clear_cache(self) -> None:
        self._compute_heavy_task.cache_clear()

    def __call__(self, batch: list[list[int]]) -> list[Any]:
        return self.process_batch(batch)
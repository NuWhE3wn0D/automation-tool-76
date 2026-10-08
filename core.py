from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class BatchExecutor:
    def __init__(self, max_workers: int = 8):
        self.max_workers = max_workers

    @lru_cache(maxsize=2048)
    def _execute_memoized(self, func: Callable[[Any], Any], arg: Any) -> Any:
        return func(arg)

    def map_parallel(self, func: Callable[[T], R], items: Iterable[T]) -> List[R]:
        unique_items = list(items)
        results = [None] * len(unique_items)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._execute_memoized, func, item): i
                for i, item in enumerate(unique_items)
            }
            for future in as_completed(futures):
                index = futures[future]
                results[index] = future.result()

        return results

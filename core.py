from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class CoreTaskProcessor:
    def __init__(self, max_workers: int = 8, cache_size: int = 2048) -> None:
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self._setup_cache(cache_size)

    def _setup_cache(self, size: int) -> None:
        @lru_cache(maxsize=size)
        def memoized_apply(func: Callable[[Any], Any], arg: Any) -> Any:
            return func(arg)

        self._memoized_apply = memoized_apply

    def map_cached(self, func: Callable[[T], R], items: Iterable[T]) -> List[R]:
        return [self._memoized_apply(func, item) for item in items]

    def process_parallel(self, func: Callable[[T], R], items: List[T], chunk_size: int = 100) -> List[R]:
        if not items:
            return []

        chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
        futures = [self.executor.submit(self._process_chunk, func, chunk) for chunk in chunks]

        results: List[R] = []
        for future in as_completed(futures):
            results.extend(future.result())
        return results

    @staticmethod
    def _process_chunk(func: Callable[[T], R], chunk: List[T]) -> List[R]:
        return [func(item) for item in chunk]

    def close(self) -> None:
        self.executor.shutdown(wait=True)

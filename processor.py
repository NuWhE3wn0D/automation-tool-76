import concurrent.futures
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class BatchProcessor:
    def __init__(self, max_workers: int = 4, chunk_size: int = 50) -> None:
        self.max_workers = max_workers
        self.chunk_size = chunk_size

    def _create_chunks(self, items: List[T]) -> List[List[T]]:
        return [
            items[i : i + self.chunk_size]
            for i in range(0, len(items), self.chunk_size)
        ]

    def map_parallel(self, func: Callable[[T], R], items: Iterable[T]) -> List[R]:
        item_list = list(items)
        if not item_list:
            return []

        chunks = self._create_chunks(item_list)
        results: List[R] = []

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            futures = [
                executor.submit(self._run_batch, func, chunk) for chunk in chunks
            ]
            for future in concurrent.futures.as_completed(futures):
                results.extend(future.result())

        return results

    @staticmethod
    def _run_batch(func: Callable[[T], R], chunk: List[T]) -> List[R]:
        return [func(item) for item in chunk]

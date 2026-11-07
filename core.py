import concurrent.futures
import functools
import itertools
from typing import Callable, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class OptimizedPipeline:
    def __init__(self, max_workers: int = 8, batch_size: int = 100):
        self.max_workers = max_workers
        self.batch_size = batch_size

    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def _cached_transform(val: str) -> str:
        return val.strip().lower()

    def _chunk_iterable(self, iterable: Iterable[T], size: int) -> Iterable[List[T]]:
        iterator = iter(iterable)
        while chunk := list(itertools.islice(iterator, size)):
            yield chunk

    def map_parallel(self, func: Callable[[T], R], items: Sequence[T]) -> List[R]:
        if not items:
            return []

        if len(items) < self.batch_size:
            return [func(item) for item in items]

        results: List[R] = []
        chunks = list(self._chunk_iterable(items, self.batch_size))

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(lambda c: [func(x) for x in c], chunk)
                for chunk in chunks
            ]
            for future in concurrent.futures.as_completed(futures):
                results.extend(future.result())
        return results

    def normalize_keys(self, keys: List[str]) -> List[str]:
        return self.map_parallel(self._cached_transform, keys)

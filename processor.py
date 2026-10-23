import concurrent.futures
from typing import Any, Callable, Generator, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class BatchProcessor:
    def __init__(self, max_workers: int = 4, chunk_size: int = 100) -> None:
        self.max_workers = max_workers
        self.chunk_size = chunk_size

    def _chunk_iterable(
        self, items: List[T]
    ) -> Generator[List[T], None, None]:
        for i in range(0, len(items), self.chunk_size):
            yield items[i : i + self.chunk_size]

    def _process_chunk(self, chunk: List[T], func: Callable[[T], R]) -> List[R]:
        return [func(item) for item in chunk]

    def process_parallel(self, items: List[T], func: Callable[[T], R]) -> List[R]:
        if not items:
            return []

        chunks = list(self._chunk_iterable(items))
        results: List[R] = []

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            futures = [
                executor.submit(self._process_chunk, chunk, func)
                for chunk in chunks
            ]
            for future in concurrent.futures.as_completed(futures):
                results.extend(future.result())

        return results


def optimize_data_pipeline(
    data: List[Any], transform_fn: Callable[[Any], Any]
) -> List[Any]:
    processor = BatchProcessor(max_workers=8, chunk_size=50)
    return processor.process_parallel(data, transform_fn)

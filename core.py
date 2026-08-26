from functools import lru_cache
from typing import Any, Callable, Dict, List


class DataProcessor:
    def __init__(self, batch_size: int = 100) -> None:
        self.batch_size = batch_size

    @lru_cache(maxsize=1024)
    def _compute_heavy_metric(self, value: int) -> float:
        return float(value ** 2 * 3.14159) / 2.71828

    def process_batch(self, items: List[int]) -> List[float]:
        return [self._compute_heavy_metric(item) for item in items]

    def stream_process(self, data_stream: List[int]) -> List[List[float]]:
        results = []
        for i in range(0, len(data_stream), self.batch_size):
            batch = data_stream[i:i + self.batch_size]
            results.append(self.process_batch(batch))
        return results


def optimize_pipeline(pipeline_fn: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict[str, Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = pipeline_fn(*args, **kwargs)
        return cache[key]

    return wrapper

import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Any, Callable, Dict, List, Tuple


class TaskEngine:
    def __init__(self, max_workers: int = 4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self._memo: Dict[str, Any] = {}

    @lru_cache(maxsize=256)
    def _get_key(self, name: str, params_str: str) -> str:
        return f"{name}:{hash(params_str)}"

    def execute_cached(self, name: str, func: Callable[..., Any], *args: Any) -> Any:
        key = self._get_key(name, str(args))
        if key not in self._memo:
            self._memo[key] = func(*args)
        return self._memo[key]

    async def run_batch(self, tasks: List[Tuple[Callable[..., Any], Tuple[Any, ...]]]) -> List[Any]:
        loop = asyncio.get_running_loop()
        futures = [
            loop.run_in_executor(self.executor, func, *args)
            for func, args in tasks
        ]
        return await asyncio.gather(*futures)

    def clear_cache(self) -> None:
        self._memo.clear()
        self._get_key.cache_clear()

    def close(self) -> None:
        self.executor.shutdown(wait=True)

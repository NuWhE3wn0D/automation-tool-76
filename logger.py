import logging
import functools
from typing import Callable, Any

class PerformanceLogger:
    _instances = {}

    def __new__(cls, name: str) -> 'PerformanceLogger':
        if name not in cls._instances:
            instance = super().__new__(cls)
            instance.logger = logging.getLogger(name)
            instance.logger.setLevel(logging.INFO)
            cls._instances[name] = instance
        return cls._instances[name]

    def __init__(self, name: str) -> None:
        self.name = name

    def timer(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            import time
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            self.logger.info(f"{func.__name__} executed in {duration:.4f}s")
            return result
        return wrapper

log = PerformanceLogger('automation-tool-76')
import logging
import functools
import time
from typing import Callable, Any

_log_cache = {}

class PerformanceLogger:
    def __init__(self, name: str = "automation-tool-76"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    @staticmethod
    def measure(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            if duration > 0.1:
                print(f"[PERF] {func.__name__} took {duration:.4f}s")
            return result
        return wrapper

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_instance() -> logging.Logger:
    if "default" not in _log_cache:
        _log_cache["default"] = PerformanceLogger().get_logger()
    return _log_cache["default"]
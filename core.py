import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(exceptions: tuple = (Exception,), retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(retries=3, delay=2.0)
def fetch_data(url: str) -> dict:
    # Simulate network call
    import requests
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
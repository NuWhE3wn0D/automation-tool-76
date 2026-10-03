import functools
import time
import logging
import urllib.request
import urllib.error

logger = logging.getLogger("automation_tool")

def retry_on_failure(exceptions, tries=3, delay=1, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"Retrying {func.__name__} in {mdelay}s due to: {e}")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry_on_failure((urllib.error.URLError, ConnectionError, TimeoutError), tries=3, delay=1, backoff=2)
def execute_network_request(url: str, timeout: int = 5) -> str:
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8")

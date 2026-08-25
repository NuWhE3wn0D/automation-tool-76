import time
import random
from functools import wraps

def retry_network_operation(max_attempts=5, initial_delay=1.0, backoff_factor=2.0, max_delay=60.0, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            delay = initial_delay
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= max_attempts:
                        raise
                    sleep_time = min(delay, max_delay)
                    time.sleep(sleep_time + random.uniform(0, 1))
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, initial_delay=0.5)
def fetch_data(url):
    if random.random() < 0.7:
        raise ConnectionError("Network failure")
    return f"Data from {url}"

if __name__ == "__main__":
    try:
        result = fetch_data("https://example.com")
        print(result)
    except Exception as e:
        print(f"Failed after retries: {e}")
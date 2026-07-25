import time
import requests

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, NetworkError) as e:
                    attempts += 1
                    if attempts == max_retries:
                        raise NetworkError('Max retries exceeded')
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
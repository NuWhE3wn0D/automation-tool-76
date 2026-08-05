import time
import requests


def retry_on_exception(max_retries, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    retries += 1
                    time.sleep(delay)
            raise e
        return wrapper
    return decorator

@retry_on_exception(max_retries=3, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

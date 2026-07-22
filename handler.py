import time
import requests

class NetworkError(Exception):
    pass

def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, NetworkError) as e:
                    if attempt < retries - 1:
                        time.sleep(delay)
                    else:
                        raise NetworkError(f'Failed after {retries} attempts') from e
        return wrapper
    return decorator

@retry_on_failure(retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    try:
        data = fetch_data('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)
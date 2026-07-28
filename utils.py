import time
import requests

class RetryException(Exception):
    pass

def retry_request(url, retries=3, backoff_factor=0.3):
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if i == retries - 1:
                raise RetryException(f'Failed after {retries} attempts') from e
            time.sleep(backoff_factor * (2 ** i))
    return None

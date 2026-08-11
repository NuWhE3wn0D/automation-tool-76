import time
import requests

class RetryException(Exception):
    pass

def retry_request(url, max_retries=3, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            retries += 1
            wait = backoff_factor * (2 ** (retries - 1))
            time.sleep(wait)
            if retries == max_retries:
                raise RetryException(f'Max retries exceeded for {url}')
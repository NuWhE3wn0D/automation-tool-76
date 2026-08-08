import time
import requests

class NetworkError(Exception):
    pass


def retry_request(url, max_retries=3, backoff_factor=0.3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            if attempt < max_retries - 1:
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                raise NetworkError(f'Failed to fetch {url} after {max_retries} attempts')

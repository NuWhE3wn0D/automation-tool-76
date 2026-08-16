import time
import requests
from requests.exceptions import RequestException

def retry_request(method, url, retries=3, backoff=1, **kwargs):
    for attempt in range(retries):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))
            else:
                raise e

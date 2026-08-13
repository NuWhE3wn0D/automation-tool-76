import time
import random

MAX_RETRIES = 5
RETRY_DELAY = 2

class NetworkError(Exception):
    pass

def retry_network_operation(operation):
    for attempt in range(MAX_RETRIES):
        try:
            return operation()
        except NetworkError:
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
                RETRY_DELAY *= 2  # exponential backoff
            else:
                raise

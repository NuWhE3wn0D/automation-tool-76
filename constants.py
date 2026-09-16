from typing import Final, Dict, Any
import os

CACHE_TTL: Final[int] = int(os.getenv('CACHE_TTL', 3600))
BATCH_SIZE: Final[int] = 1000
MAX_WORKERS: Final[int] = os.cpu_count() or 4

HTTP_TIMEOUT: Final[float] = 30.0
RETRY_ATTEMPTS: Final[int] = 3

DEFAULT_CONFIG: Final[Dict[str, Any]] = {
    'optimization_level': 2,
    'use_fast_math': True,
    'memory_limit_mb': 512,
    'concurrency_mode': 'async'
}

CACHE_ENABLED: Final[bool] = True
CHUNK_SIZE: Final[int] = 4096

__all__ = [
    'CACHE_TTL',
    'BATCH_SIZE',
    'MAX_WORKERS',
    'HTTP_TIMEOUT',
    'RETRY_ATTEMPTS',
    'DEFAULT_CONFIG',
    'CACHE_ENABLED',
    'CHUNK_SIZE'
]
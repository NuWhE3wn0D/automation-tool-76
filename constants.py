from typing import Final

import os
import multiprocessing

# System resource optimization constants
CACHE_SIZE: Final[int] = 1024
WORKER_COUNT: Final[int] = multiprocessing.cpu_count()
CHUNK_SIZE: Final[int] = 4096

# Performance thresholds
TIMEOUT_THRESHOLD: Final[float] = 30.0
BUFFER_THRESHOLD: Final[int] = 65536

# Path constants for I/O operations
BASE_PATH: Final[str] = os.getenv("APP_BASE_PATH", "/var/lib/automation")
TEMP_DIR: Final[str] = os.path.join(BASE_PATH, "tmp")

# Network optimization
MAX_RETRIES: Final[int] = 3
CONNECTION_POOL_SIZE: Final[int] = 20

# Serialization settings
ENABLE_COMPRESSION: Final[bool] = True
SERIALIZATION_LEVEL: Final[int] = 6
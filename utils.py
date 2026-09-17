import functools
import time
import logging
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)


def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mdelay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(
                            f"Function {func.__name__} failed after {tries} attempts: {e}"
                        )
                        raise
                    logger.warning(
                        f"Retrying {func.__name__} in {mdelay:.2f} seconds... "
                        f"(Attempt {attempt}/{tries}) due to {e}"
                    )
                    time.sleep(mdelay)
                    mdelay *= backoff
        return wrapper
    return decorator

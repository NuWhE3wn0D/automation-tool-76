import time
from typing import Any, Callable, Dict, Optional

def retry(attempts: int = 3, delay: float = 1.0) -> Callable:
    """Decorator for retrying functions upon failure."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_ex: Optional[Exception] = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(delay)
            raise last_ex if last_ex else Exception("Retry failed")
        return wrapper
    return decorator

def format_payload(data: Dict[str, Any]) -> str:
    """Converts dictionary data into a clean string format."""
    items = [f"{k}: {v}" for k, v in data.items()]
    return " | ".join(items)

def validate_input(value: Optional[str]) -> bool:
    """Checks if provided input is non-empty."""
    return bool(value and value.strip())
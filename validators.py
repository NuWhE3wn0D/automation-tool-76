import functools
import re
from typing import Any, Callable, Dict

_CACHE: Dict[str, Any] = {}
_EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


def memoize_validator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        key = f"{func.__name__}:{args}"
        if key not in _CACHE:
            _CACHE[key] = func(*args)
        return _CACHE[key]
    return wrapper


@memoize_validator
def validate_email_format(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_REGEX.match(email))


def batch_validate_emails(emails: list[str]) -> list[bool]:
    return [validate_email_format(e) for e in emails]


def clear_validation_cache() -> None:
    _CACHE.clear()
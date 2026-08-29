import re
from typing import Any, Callable, Dict, List

class InputValidator:
    def __init__(self) -> None:
        self._rules: Dict[str, Callable[[Any], bool]] = {}

    def register(self, name: str, validator: Callable[[Any], bool]) -> None:
        if name in self._rules:
            raise ValueError(f"Rule {name} already exists")
        self._rules[name] = validator

    def validate(self, data: Dict[str, Any]) -> Dict[str, List[str]]:
        results: Dict[str, List[str]] = {}
        for field, value in data.items():
            if field not in self._rules:
                results[field] = ["No validator registered"]
                continue
            if not self._rules[field](value):
                results[field] = ["Validation failed"]
            else:
                results[field] = []
        return {k: v for k, v in results.items() if v}

    def is_valid(self, data: Dict[str, Any]) -> bool:
        return len(self.validate(data)) == 0

def positive_integer(value: Any) -> bool:
    return isinstance(value, int) and value > 0

def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def valid_email(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, value) is not None

def valid_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?$"
    return re.match(pattern, value) is not None

def valid_port(value: Any) -> bool:
    if not isinstance(value, int):
        return False
    return 1 <= value <= 65535

def valid_timeout(value: Any) -> bool:
    if not isinstance(value, (int, float)):
        return False
    return 0 < value <= 3600

def in_range(min_val: float, max_val: float) -> Callable[[Any], bool]:
    def checker(value: Any) -> bool:
        if not isinstance(value, (int, float)):
            return False
        return min_val <= value <= max_val
    return checker

def validate_config(config: Dict[str, Any], validator: InputValidator) -> bool:
    if not isinstance(config, dict):
        return False
    return validator.is_valid(config)
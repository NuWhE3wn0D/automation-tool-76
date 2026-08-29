import os
import json
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class AutomationConfig:
    api_key: str
    base_url: str = "https://api.example.com"
    timeout: int = 30
    max_retries: int = 3
    log_level: str = "INFO"
    extra_settings: Dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.api_key:
            raise ValueError("API key is required")
        if self.timeout <= 0:
            raise ValueError("Timeout must be positive")
        if self.max_retries < 0:
            raise ValueError("Max retries must be non-negative")

def load_from_env() -> AutomationConfig:
    api_key = os.environ.get("AUTOMATION_API_KEY", "")
    base_url = os.environ.get("AUTOMATION_BASE_URL", "https://api.example.com")
    timeout = int(os.environ.get("AUTOMATION_TIMEOUT", 30))
    max_retries = int(os.environ.get("AUTOMATION_MAX_RETRIES", 3))
    log_level = os.environ.get("AUTOMATION_LOG_LEVEL", "INFO").upper()
    extra = {}
    for key, value in os.environ.items():
        if key.startswith("AUTOMATION_EXTRA_"):
            extra[key[17:].lower()] = value
    config = AutomationConfig(
        api_key=api_key,
        base_url=base_url,
        timeout=timeout,
        max_retries=max_retries,
        log_level=log_level,
        extra_settings=extra,
    )
    config.validate()
    return config

def load_from_file(filepath: str) -> AutomationConfig:
    with open(filepath, "r") as f:
        data = json.load(f)
    config = AutomationConfig(
        api_key=data.get("api_key", ""),
        base_url=data.get("base_url", "https://api.example.com"),
        timeout=data.get("timeout", 30),
        max_retries=data.get("max_retries", 3),
        log_level=data.get("log_level", "INFO").upper(),
        extra_settings=data.get("extra_settings", {}),
    )
    config.validate()
    return config

def get_config(source: str = "env", filepath: Optional[str] = None) -> AutomationConfig:
    if source == "env":
        return load_from_env()
    elif source == "file" and filepath:
        return load_from_file(filepath)
    else:
        raise ValueError("Invalid config source or missing filepath")

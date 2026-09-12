import os
from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    if not isinstance(url, str) or not url.strip():
        return False
    try:
        parsed = urlparse(url.strip())
        return all([parsed.scheme in ('http', 'https'), parsed.netloc])
    except (ValueError, AttributeError):
        return False

def validate_safe_path(base_dir: str, target_path: str) -> bool:
    if not isinstance(base_dir, str) or not isinstance(target_path, str):
        return False
    try:
        absolute_base = os.path.abspath(base_dir)
        absolute_target = os.path.abspath(os.path.join(base_dir, target_path))
        return absolute_target.startswith(absolute_base)
    except (ValueError, OSError):
        return False

def validate_config_dict(config: dict, schema: dict) -> bool:
    if not isinstance(config, dict) or not isinstance(schema, dict):
        return False
    for key, expected_type in schema.items():
        if key not in config:
            return False
        if not isinstance(config[key], expected_type):
            return False
    return True
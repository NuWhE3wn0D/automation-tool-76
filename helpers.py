import os
import json
import logging
from pathlib import Path
from typing import Any, Dict

def load_json(path: str) -> Dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    with open(path_obj, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def get_env_var(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
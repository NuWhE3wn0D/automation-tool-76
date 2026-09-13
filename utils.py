import os
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


def ensure_directory(path: str | Path) -> Path:
    target_path = Path(path)
    target_path.mkdir(parents=True, exist_ok=True)
    return target_path


def get_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json_file(file_path: str | Path) -> Dict[str, Any]:
    path = Path(file_path)
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_json_file(file_path: str | Path, data: Dict[str, Any]) -> bool:
    path = Path(file_path)
    try:
        ensure_directory(path.parent)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except (OSError, TypeError):
        return False


def get_env_var(key: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(key, default)

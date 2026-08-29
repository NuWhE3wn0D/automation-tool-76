import json
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigurationLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults: Dict[str, Any] = defaults or {}
        self.config: Dict[str, Any] = {}

    def load(self, source: Optional[str] = None) -> None:
        if source is None:
            self.config = {}
            return
        path = Path(source)
        if path.exists() and path.is_file():
            with path.open(encoding="utf-8") as f:
                self.config = json.load(f)
        else:
            self.config = {}

    def apply_defaults(self) -> Dict[str, Any]:
        result = self.defaults.copy()
        result.update(self.config)
        return result

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        if key in self.config:
            return self.config[key]
        if key in self.defaults:
            return self.defaults[key]
        return default

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value

    def reset(self) -> None:
        self.config = {}

    def save(self, destination: str) -> None:
        path = Path(destination)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def merge(self, other: Dict[str, Any]) -> None:
        self.config.update(other)
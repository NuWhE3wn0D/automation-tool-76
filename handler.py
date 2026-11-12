from typing import List, Dict, Any, Optional

class DataHandler:
    """Manages data processing and transformation tasks."""

    def __init__(self, source: str) -> None:
        self.source: str = source
        self.cache: Dict[str, Any] = {}

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Transforms a list of dictionaries by applying internal rules."""
        return [self._sanitize(item) for item in items]

    def _sanitize(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Cleans individual data entries."""
        return {k: str(v).strip() for k, v in item.items()}

    def get_cached_item(self, key: str) -> Optional[Any]:
        """Retrieves an item from the internal cache by key."""
        return self.cache.get(key)

    def update_cache(self, key: str, value: Any) -> None:
        """Updates the internal cache with new data."""
        self.cache[key] = value

    def clear_cache(self) -> None:
        """Resets the internal cache storage."""
        self.cache.clear()
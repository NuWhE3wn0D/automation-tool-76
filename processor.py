from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles transformation and validation of automation data."""

    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings: Dict[str, Any] = settings

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Applies transformation rules to a list of items."""
        return [self._transform(item) for item in items if self._is_valid(item)]

    def _transform(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Normalizes item keys based on configuration."""
        transformed = item.copy()
        transformed["processed"] = True
        return transformed

    def _is_valid(self, item: Dict[str, Any]) -> bool:
        """Validates item integrity against schema requirements."""
        required_fields = self.settings.get("required", [])
        return all(field in item for field in required_fields)

    def get_summary(self, results: List[Dict[str, Any]]) -> Optional[str]:
        """Generates string summary of processing results."""
        if not results:
            return None
        return f"Processed {len(results)} items successfully"
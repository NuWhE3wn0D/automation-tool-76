from typing import Any, Dict, List, Optional


def validate_item(item: Dict[str, Any]) -> bool:
    if not isinstance(item, dict):
        return False
    if "id" not in item or not isinstance(item["id"], (int, str)):
        return False
    if "action" not in item or not isinstance(item["action"], str):
        return False
    return True


class DataProcessor:
    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        self.config = config or {}
        self.processed_count = 0
        self.errors: List[Dict[str, Any]] = []

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = []
        for idx, item in enumerate(items):
            if not validate_item(item):
                self.errors.append({"index": idx, "item": item, "reason": "Invalid payload format"})
                continue

            processed = self._execute_task(item)
            results.append(processed)
            self.processed_count += 1

        return results

    def _execute_task(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "id": item["id"],
            "status": "completed",
            "result": f"Executed action '{item['action']}' successfully"
        }

from typing import Any, Dict, List, Tuple


def validate_item(item: Any) -> Tuple[bool, str]:
    if not isinstance(item, dict):
        return False, "item must be a dictionary"
    if "id" not in item or not str(item["id"]).strip():
        return False, "missing or empty 'id' field"
    if "task" not in item or not isinstance(item["task"], str):
        return False, "missing or non-string 'task' field"
    if not item["task"].strip():
        return False, "'task' field cannot be blank"
    return True, ""


class ProcessingEngine:
    def __init__(self) -> None:
        self.processed_count = 0
        self.failed_count = 0

    def run(self, payload: List[Any]) -> Dict[str, Any]:
        results: List[Dict[str, Any]] = []
        errors: List[Dict[str, Any]] = []

        for raw_item in payload:
            is_valid, error_reason = validate_item(raw_item)
            if not is_valid:
                self.failed_count += 1
                errors.append({"raw_input": raw_item, "reason": error_reason})
                continue

            processed_entry = {
                "id": str(raw_item["id"]).strip(),
                "task": raw_item["task"].strip().lower(),
                "status": "success",
            }
            results.append(processed_entry)
            self.processed_count += 1

        return {
            "processed": results,
            "errors": errors,
            "total_processed": self.processed_count,
            "total_failed": self.failed_count,
        }

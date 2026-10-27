from typing import Any, Callable, Dict, List, Optional


class BatchProcessor:
    def __init__(self, batch_size: int = 100) -> None:
        self.batch_size = max(1, batch_size)
        self._hooks: List[Callable[[List[Any]], List[Any]]] = []

    def register_hook(self, hook: Callable[[List[Any]], List[Any]]) -> None:
        if callable(hook):
            self._hooks.append(hook)

    def _apply_hooks(self, chunk: List[Any]) -> List[Any]:
        result = chunk
        for hook in self._hooks:
            result = hook(result)
        return result

    def process(self, items: List[Any]) -> List[Any]:
        if not items:
            return []

        processed: List[Any] = []
        for i in range(0, len(items), self.batch_size):
            chunk = items[i : i + self.batch_size]
            transformed = self._apply_hooks(chunk)
            processed.extend(transformed)

        return processed


def sanitize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    return {
        k.strip().lower(): (v.strip() if isinstance(v, str) else v)
        for k, v in record.items()
        if k is not None
    }


def filter_empty_values(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {k: v for k, v in item.items() if v is not None and v != ""}
        for item in items
    ]

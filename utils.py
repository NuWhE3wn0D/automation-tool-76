from typing import Any, Dict, Iterable, List, Generator


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def chunk_iterable(
    iterable: Iterable[Any], size: int
) -> Generator[List[Any], None, None]:
    if size < 1:
        raise ValueError("Chunk size must be at least 1")
    chunk: List[Any] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def sanitize_data(data: Any) -> Any:
    if isinstance(data, dict):
        cleaned = {}
        for k, v in data.items():
            if v is not None:
                res = sanitize_data(v)
                if res != {} and res != []:
                    cleaned[k] = res
        return cleaned
    if isinstance(data, list):
        return [
            sanitize_data(item)
            for item in data
            if item is not None and sanitize_data(item) not in ({}, [])
        ]
    return data

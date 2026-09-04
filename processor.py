from typing import Any, Dict, Generator, Iterable, List, Type


def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    iterator = iter(iterable)
    while True:
        chunk = []
        try:
            for _ in range(size):
                chunk.append(next(iterator))
            yield chunk
        except StopIteration:
            if chunk:
                yield chunk
            break


def deep_merge(dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> Dict[Any, Any]:
    result = dict_a.copy()
    for key, value in dict_b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def flatten(items: Iterable[Any]) -> List[Any]:
    flat_list = []
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def safe_cast(value: Any, to_type: Type[Any], default: Any = None) -> Any:
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default

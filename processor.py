from typing import Any, Dict, List, Union

def sanitize_data(data: Union[Dict, List]) -> Union[Dict, List]:
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data if i is not None]
    return data

def flatten_data(data: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_data(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def batch_process(items: List[Any], chunk_size: int = 100) -> List[List[Any]]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
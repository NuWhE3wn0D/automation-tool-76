import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

def read_file(filepath: Union[str, Path]) -> str:
    """Read content from a file.

    Args:
        filepath: Path to the file.
    Returns:
        Content of the file.
    """
    path = Path(filepath)
    with path.open('r', encoding='utf-8') as file:
        return file.read()

def write_file(filepath: Union[str, Path], content: str) -> None:
    """Write content to a file.

    Args:
        filepath: Path to the file.
        content: Content to write.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as file:
        file.write(content)

def parse_json(data: str) -> Dict[str, Any]:
    """Parse a JSON string.

    Args:
        data: The JSON string.
    Returns:
        The parsed dict.
    """
    return json.loads(data)

def serialize_json(data: Dict[str, Any], indent: Optional[int] = None) -> str:
    """Serialize to JSON string.

    Args:
        data: The data dict.
        indent: Optional indent.
    Returns:
        The JSON string.
    """
    return json.dumps(data, indent=indent)

def find_items(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Find matching items.

    Args:
        data: List of dicts.
        key: Key for match.
        value: Value for match.
    Returns:
        List of matches.
    """
    return [item for item in data if item.get(key) == value]
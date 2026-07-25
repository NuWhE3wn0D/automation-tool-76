from typing import Any, Dict, List


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges two dictionaries, with values from dict2 overwriting those in dict1.

    Args:
        dict1 (Dict[str, Any]): The first dictionary.
        dict2 (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: The merged dictionary.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (List[List[Any]]): The nested list to flatten.

    Returns:
        List[Any]: A flat list containing all elements.
    """
    return [item for sublist in nested_list for item in sublist]


def check_key_exists(dictionary: Dict[str, Any], key: str) -> bool:
    """
    Checks if a key exists in the given dictionary.

    Args:
        dictionary (Dict[str, Any]): The dictionary to check.
        key (str): The key to check for.

    Returns:
        bool: True if the key exists, else False.
    """
    return key in dictionary

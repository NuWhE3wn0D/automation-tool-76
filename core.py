from typing import List, Dict


def process_data(data: List[Dict[str, str]]) -> List[str]:
    """
    Process a list of dictionaries and extract values.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries containing string key-value pairs.

    Returns:
        List[str]: A list of processed string values.
    """
    return [item['value'] for item in data if 'value' in item]


def calculate_average(values: List[float]) -> float:
    """
    Calculate the average of a list of float values.

    Args:
        values (List[float]): A list of float values.

    Returns:
        float: The average value, or 0 if the list is empty.
    """
    return sum(values) / len(values) if values else 0.0


def filter_valid_data(data: List[Dict[str, str]], key: str) -> List[Dict[str, str]]:
    """
    Filter out dictionaries that do not contain the specified key.

    Args:
        data (List[Dict[str, str]]): The list of dictionaries to filter.
        key (str): The key to check for in each dictionary.

    Returns:
        List[Dict[str, str]]: A list of filtered dictionaries.
    """
    return [item for item in data if key in item]
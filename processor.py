from typing import List, Dict


def process_data(data: List[Dict[str, int]]) -> List[Dict[str, int]]:
    """Process a list of dictionaries to double each value.

    Args:
        data (List[Dict[str, int]]): A list of dictionaries with integer values.

    Returns:
        List[Dict[str, int]]: A new list with each value doubled.
    """
    return [{k: v * 2 for k, v in item.items()} for item in data]


def log_processed_data(data: List[Dict[str, int]], logger) -> None:
    """Log each processed data entry.

    Args:
        data (List[Dict[str, int]]): A list of processed dictionaries.
        logger: Logger instance to log data.
    """
    for item in data:
        logger.info(item)
from typing import List, Optional


def find_max(numbers: List[Optional[int]]) -> Optional[int]:
    """Returns the maximum number from a list of integers.

    Args:
        numbers (List[Optional[int]]): A list of integers, which can include None.

    Returns:
        Optional[int]: The maximum integer in the list, or None if the list is empty or contains only None.
    """
    filtered_numbers = [num for num in numbers if num is not None]
    return max(filtered_numbers) if filtered_numbers else None


def calculate_average(numbers: List[Optional[float]]) -> Optional[float]:
    """Calculates the average of a list of floats.

    Args:
        numbers (List[Optional[float]]): A list of floating point numbers, which can include None.

    Returns:
        Optional[float]: The average of the numbers, or None if the list is empty or contains only None.
    """
    filtered_numbers = [num for num in numbers if num is not None]
    return sum(filtered_numbers) / len(filtered_numbers) if filtered_numbers else None


def format_string(value: str, prefix: str = '', suffix: str = '') -> str:
    """Formats a string by adding a prefix and/or suffix.

    Args:
        value (str): The string to format.
        prefix (str, optional): The prefix to add. Defaults to ''.
        suffix (str, optional): The suffix to add. Defaults to ''.

    Returns:
        str: The formatted string with prefix and suffix.
    """
    return f'{prefix}{value}{suffix}'
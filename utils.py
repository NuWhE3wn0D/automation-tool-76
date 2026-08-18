from typing import List, Dict


def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def filter_dictionary(data: Dict[str, int], threshold: int) -> Dict[str, int]:
    """Filter a dictionary by a threshold value."""
    return {key: value for key, value in data.items() if value > threshold}


def format_string(template: str, **kwargs: Dict[str, str]) -> str:
    """Format a string with given keyword arguments."""
    return template.format(**kwargs)


def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    """Merge two lists into one, avoiding duplicates."""
    return list(set(list1 + list2))


def get_unique_elements(elements: List[int]) -> List[int]:
    """Return a list of unique elements from the input list."""
    return list(set(elements))
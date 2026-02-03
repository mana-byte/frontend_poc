def get_max_from_data(data: list[dict[str, int | str]], key: str):
    """Get the maximum value from a list of dictionaries for a specific key.
    Args:
        data (list[dict[str, int | str]]): The list of dictionaries containing the data.
        key (str): The key to look for in the dictionaries.
    Returns:
        int: The maximum value found for the specified key.
    """
    return max(item[key] for item in data if key in item and isinstance(item[key], int))


def get_min_from_data(data: list[dict[str, int | str]], key: str):
    """Get the minimum value from a list of dictionaries for a specific key.
    Args:
        data (list[dict[str, int | str]]): The list of dictionaries containing the data.
        key (str): The key to look for in the dictionaries.
    Returns:
        int: The minimum value found for the specified key.
    """
    return min(item[key] for item in data if key in item and isinstance(item[key], int))

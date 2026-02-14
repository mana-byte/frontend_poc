def get_max_from_data(data: list[dict[str, int | str]], key: str):
    """Get the maximum value from a list of dictionaries for a specific key.
    Args:
        data (list[dict[str, int | str]]): The list of dictionaries containing the data.
        key (str): The key to look for in the dictionaries.
    Returns:
        int: The maximum value found for the specified key.
    """
    if data == []:
        return 0
    return max(item[key] for item in data if key in item and isinstance(item[key], int))


def get_min_from_data(data: list[dict[str, int | str]], key: str):
    """Get the minimum value from a list of dictionaries for a specific key.
    Args:
        data (list[dict[str, int | str]]): The list of dictionaries containing the data.
        key (str): The key to look for in the dictionaries.
    Returns:
        int: The minimum value found for the specified key.
    """
    if data == []:
        return 0
    return min(item[key] for item in data if key in item and isinstance(item[key], int))


def fetch_data_from_api(api_url: str) -> list[dict[str, int | str]]:
    """Fetch data from a given API URL.
    Args:
        api_url (str): The URL of the API to fetch data from.
    Returns:
        list[dict[str, int | str]]: The data fetched from the API.
    """
    import requests
    import logging

    # Configure logging
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger(__name__)
    response = requests.get(api_url)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Error fetching data from API: {e}")
        logger.error(f"Error fetching data from API: {e}", exc_info=True)
        return []
    return response.json()

from dash import html
import dash_mantine_components as dmc
from components.linechart import linechart
from components.calendar import calendar
from components.keypoints import keypoints

default_data = [
    {"date": "09:00", "today": 80, "yesterday": 70},
    {"date": "10:00", "today": 100, "yesterday": 90},
    {"date": "11:00", "today": 120, "yesterday": 110},
    {"date": "12:00", "today": 150, "yesterday": 130},
    {"date": "13:00", "today": 160, "yesterday": 140},
    {"date": "14:00", "today": 180, "yesterday": 150},
    {"date": "15:00", "today": 170, "yesterday": 160},
]


def home(id: str, data: list[dict[str, int | str]] = default_data) -> html.Div:
    """Groups all of the main data components together into a single layout
    Args:
        id (str): The unique identifier for the home component.
        data (list[dict[str, int | str]], optional): The data to be displayed
    Returns:
        html.Div: A Dash HTML Div containing the keypoints, linechart, and calendar components.
    """
    return html.Div(
        [
            keypoints(id=f"{id}-keypoints", data=data),
            linechart(id=f"{id}-linechart", data=data),
            calendar(id=f"{id}-calendar"),
        ],
        className="home",
        id=id,
    )

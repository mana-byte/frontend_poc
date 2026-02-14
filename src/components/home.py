from dash import html
import dash_mantine_components as dmc
from components.linechart import linechart
from components.calendar import calendar
from components.keypoints import keypoints

default_data = [
    {"time": "09:00", "nb_people": 100},
    {"time": "10:00", "nb_people": 120},
    {"time": "11:00", "nb_people": 69},
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

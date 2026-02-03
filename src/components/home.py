from dash import html
import dash_mantine_components as dmc
from components.linechart import linechart

default_data = [
    {"date": "09:00", "today": 80, "yesterday": 70},
    {"date": "10:00", "today": 100, "yesterday": 90},
    {"date": "11:00", "today": 120, "yesterday": 110},
    {"date": "12:00", "today": 150, "yesterday": 130},
    {"date": "13:00", "today": 160, "yesterday": 140},
    {"date": "14:00", "today": 180, "yesterday": 150},
    {"date": "15:00", "today": 170, "yesterday": 160},
]


def home(id: str, data: list[dict[str, int | str]] = default_data):
    return html.Div(
        [linechart(id=f"{id}-linechart", data=data)],
        className="home",
        id=id,
    )

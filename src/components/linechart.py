import dash_mantine_components as dmc
from utils import get_max_from_data, get_min_from_data
from datetime import datetime, timedelta


def linechart(
    id: str, data: list[dict[str, int | str]], key: str = "nb_people"
) -> dmc.LineChart:
    return dmc.LineChart(
        h=300,
        strokeWidth=4,
        # Data
        dataKey="time",
        data=data,
        # Disable axes
        withXAxis=False,
        withYAxis=False,
        yAxisProps={
            "domain": [get_min_from_data(data, key), get_max_from_data(data, key)]
        },
        # Legend
        legendProps={"verticalAlign": "bottom"},
        withLegend=True,
        # Animation
        tooltipAnimationDuration=500,
        lineProps={
            "isAnimationActive": True,
            "animationDuration": 1000,
            "animationEasing": "ease-in-out",
            "animationBegin": 1000,
        },
        series=[
            {"name": "nb_people", "label": "Nombre de personnes", "color": "#667eea"},
        ],
        className="graph",
        id="linechart",
    )

def format_datetime(date: str) -> str:
    today = datetime.today().strftime("%Y-%m-%d")
    if date == today:
        return "Aujourd'hui"
    if date == (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d"):
        return "Hier"
    else:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%d %B %Y")

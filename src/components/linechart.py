import dash_mantine_components as dmc
from utils import get_max_from_data, get_min_from_data


def linechart(id: str, data: list[dict[str, int | str]], key: str = "today"):
    return dmc.LineChart(
        h=300,
        strokeWidth=4,
        # Data
        dataKey="date",
        data=data,
        # Disable axes
        withXAxis=False,
        withYAxis=False,
        yAxisProps={"domain": [get_min_from_data(data, key), get_max_from_data(data, key)]},
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
            {"name": "today", "label": "Today", "color": "#667eea"},
            {
                "name": "yesterday",
                "label": "Yesterday",
                "color": "#764ba2",
            },
        ],
        className="graph",
        id="linechart",
    )

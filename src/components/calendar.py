import dash_mantine_components as dmc
from dash import callback, Input, Output
from datetime import datetime


def calendar(id: str):
    default_date = datetime.today().strftime('%Y-%m-%d')
    return dmc.Stack(
        [
            dmc.MiniCalendar(
                defaultDate=default_date, 
                value=default_date, 
                id="mini-calendar",
            ),
            dmc.Text(id="mini-calendar-date", m="md"),
        ],
        className="calendar-container"
    )


@callback(
    Output("mini-calendar-date", "children"),
    Input("mini-calendar", "value"),
)
def update(d):
    return f"You selected: {d}"

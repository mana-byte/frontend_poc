import dash_mantine_components as dmc
from datetime import datetime


def calendar(id: str) -> dmc.Stack:
    """Creates a calendar component using Dash Mantine Components.
    Args:
        id (str): The unique identifier for the calendar component.
    Returns:
        dmc.Stack: A Dash Mantine Stack containing the calendar and a text element to display the selected date.
    """
    default_date = datetime.today().strftime("%Y-%m-%d")
    return dmc.Stack(
        [
            dmc.MiniCalendar(
                defaultDate=default_date,
                value=default_date,
                id="mini-calendar",
                style={"margin": "20px"},
                numberOfDays=9,
                locale="fr",
            ),
        ],
        className="calendar-container",
    )



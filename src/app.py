from dash import Dash, callback, Output, Input
import dash_mantine_components as dmc
import components.nav as nav
import components.home as home
import components.slide_modal as slide_modal
import os
from utils import fetch_data_from_api

app = Dash()
API_URL = os.getenv("API_URL", "http://localhost:6942/")
API_ROUTE_TODAY = os.getenv("API_ROUTE", "get_today")
API_ROUTE_YESTERDAY = os.getenv("API_ROUTE", "get_yesterday")

data = fetch_data_from_api(API_URL + API_ROUTE_TODAY)[::-1]

app.layout = dmc.MantineProvider(
    [
        nav.navbar(id="navbar-component"),
        home.home(id="home-component", data=data),
        slide_modal.slide_modal(id="slide-modal-component"),
    ],
    # theme=dark_theme.theme,
    forceColorScheme="light",
    id="mantine-provider",
)


@callback(
    Output("mantine-provider", "forceColorScheme"), Input("theme-switch", "checked")
)
def toggle_theme(checked) -> str:
    return "light" if checked else "dark"


@callback(
    Output("charm:chevrons-up", "color"),
    Input("theme-switch", "checked"),
)
def icon_color(checked) -> str:
    return "#000" if checked else "#fff"


if __name__ == "__main__":
    app.run(debug=True)

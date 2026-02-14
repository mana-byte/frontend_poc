from dash import Dash, callback, Output, Input
import dash_mantine_components as dmc
import components.nav as nav
import components.home as home
import components.slide_modal as slide_modal
import os

app = Dash()
API_URL = os.getenv("API_URL", "http://localhost:8000/api/data")

app.layout = dmc.MantineProvider(
    [
        nav.navbar(id="navbar-component"),
        home.home(id="home-component"),
        slide_modal.slide_modal(id="slide-modal-component"),
    ],
    # theme=dark_theme.theme,
    forceColorScheme="light",
    id="mantine-provider",
)


@callback(
    Output("mantine-provider", "forceColorScheme"), Input("theme-switch", "checked")
)
def toggle_theme(checked):
    return "light" if checked else "dark"


@callback(
    Output("charm:chevrons-up", "color"),
    Input("theme-switch", "checked"),
)
def icon_color(checked):
    return "#000" if checked else "#fff"


if __name__ == "__main__":
    app.run(debug=True)

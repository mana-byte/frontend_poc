from dash import Dash, html, callback, Output, Input
import dash_mantine_components as dmc
import components.nav as nav
import components.home as home
import components.slide_modal as slide_modal

app = Dash()

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
    return "dark" if not checked else "light"


if __name__ == "__main__":
    app.run(debug=True)

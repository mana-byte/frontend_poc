from dash import Dash, dcc, html
import dash_mantine_components as dmc

import components.nav as nav
import components.home as home
import components.slide_modal as slide_modal

# Required callbacks to make the app work
import callbacks.theme
import callbacks.data_update

app = Dash()

app.layout = html.Div(
    dmc.MantineProvider(
        [
            # data store
            dcc.Store(id="data-store"),
            # Website
            nav.navbar(id="navbar-component"),
            home.home(id="home-component"),
            slide_modal.slide_modal(id="slide-modal-component"),
        ],
        forceColorScheme="light",
        id="mantine-provider",
    ),
    id="app-container",
)

if __name__ == "__main__":
    app.run(debug=True)

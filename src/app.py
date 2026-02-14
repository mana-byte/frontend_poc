from dash import Dash, html
import dash_mantine_components as dmc
import components.nav as nav
import components.home as home

app = Dash()

app.layout = dmc.MantineProvider(
    [
        html.Div(id="output"),
        nav.navbar(id="navbar-component"),
        dmc.Space(h=80),  # Add space for fixed navbar
        home.home(id="home-component"),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

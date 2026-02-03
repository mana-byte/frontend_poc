from dash import Dash, html, callback, Output, Input
import dash_mantine_components as dmc
import components.nav as nav_component

app = Dash()

app.layout = dmc.MantineProvider(
    [
        nav_component.nav(id="main-nav"),
        html.Div(id="output")
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

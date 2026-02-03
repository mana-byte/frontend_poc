from dash import html, Output, Input, callback
import dash_mantine_components as dmc


def nav(id: str):
    return html.Div(
        [dmc.Burger(id="burger-button", opened=False), dmc.Text(id="burger-state", mt="md")]
    )


@callback(Output("burger-state", "children"), Input("burger-button", "opened"))
def is_open(opened):
    return str(opened)

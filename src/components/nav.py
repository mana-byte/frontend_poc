from dash import html, Output, Input, callback
import dash_mantine_components as dmc


def home(id: str):
    return html.Div(["hello"], className="home", id=id)

from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def navbar(id: str):
    return html.Div(
        className="navbar-container",
        children=[
            # Logo/Brand
            html.Div(className="navbar-logo", children="DOIT"),
            # Navigation links
            html.Div(
                className="nav-links",
                children=[
                    dmc.Switch(
                        offLabel=DashIconify(icon="radix-icons:moon", width=20),
                        onLabel=DashIconify(icon="radix-icons:sun", width=20),
                        size="xl",
                        id="theme-switch"
                    ),
                    dmc.Anchor(
                        className="nav-link",
                        children=[DashIconify(icon="ion:logo-github", width=50)],
                        href="https://github.com/mana-byte/frontend_poc",
                    ),
                ],
            ),
        ],
        id=id,
    )

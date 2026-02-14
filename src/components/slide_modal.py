from dash import html, Input, Output, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def slide_modal(id: str) -> html.Div:
    """Creates a slide-up modal component using Dash HTML, Dash Mantine Components, and Dash Iconify.
    Args:
        id (str): The unique identifier for the slide modal component.
    Returns:
        html.Div: A Dash HTML Div containing a button to open the modal and the modal itself with an image.

    """
    return html.Div(
        [
            html.Div(
                dmc.Button(
                    [
                        DashIconify(
                            id="charm:chevrons-up",
                            icon="charm:chevrons-up",
                            width=30,
                            color="white",
                        )
                    ],
                    id="open-modal",
                    className="bottom-button",
                ),
                className="fixed-button-container",
            ),
            dmc.Modal(
                id="slide-modal",
                children=[
                    dmc.Image(
                        radius="md",
                        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-7.png",
                    )
                ],
                zIndex=1000,
                fullScreen=True,
                transitionProps={"duration": 1000, "transition": "slide-up"},
            ),
        ]
    )


@callback(
    Output("slide-modal", "opened"),
    Input("open-modal", "n_clicks"),
    prevent_initial_call=True,
)
def open_modal(n_clicks):
    return True

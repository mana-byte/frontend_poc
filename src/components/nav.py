from dash import html

def navbar(id: str):
    return html.Div(
        className="navbar-container",
        children=[
            # Logo/Brand
            html.Div(
                className="navbar-logo",
                children="Data Dashboard",
            ),
            
            # Navigation links
            html.Div(
                className="nav-links",
                children=[
                    html.Button(
                        className="nav-link",
                        children=[
                            html.Span("Home"),
                            html.Span(""),
                        ],
                    ),
                    html.Button(
                        className="nav-link",
                        children=[
                            html.Span("Analytics"),
                            html.Span(""),
                        ],
                    ),
                    html.Button(
                        className="nav-link",
                        children=[
                            html.Span("Settings"),
                            html.Span(""),
                        ],
                    ),
                ],
            ),
        ],
        id=id,
    )

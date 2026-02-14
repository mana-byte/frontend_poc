from dash import callback, Output, Input


@callback(
    Output("mantine-provider", "forceColorScheme"), Input("theme-switch", "checked")
)
def toggle_theme(checked) -> str:
    return "light" if checked else "dark"


@callback(
    Output("charm:chevrons-up", "color"),
    Input("theme-switch", "checked"),
)
def icon_color(checked) -> str:
    return "#000" if checked else "#fff"

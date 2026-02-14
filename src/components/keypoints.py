import dash_mantine_components as dmc
from utils import get_max_from_data, get_min_from_data


def keypoints(
    id: str, data: list[dict[str, int | str]], key: str = "nb_people"
) -> dmc.Group:
    """Creates cards based on given data giving the maximum and current values
    Args:
        id (str): The unique identifier for the keypoints component.
        data (list[dict[str, int | str]]): The data to be displayed in the keypoints.
        key (str, optional): The key to look for in the data dictionaries. Defaults to "today".
    Returns:
        dmc.Group: A Dash Mantine Group containing the keypoint cards.
    """
    if data and key in data[0]:
        max_value = get_max_from_data(data, key)
        return dmc.Group(
            [
                dmc.Card(
                    [
                        dmc.Text("Actuellement", size="xs"),
                        dmc.Text(id="current_nb_text" ,children=f"{data[-1:][0]['nb_people']}", size="xl"),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    padding="md",
                    className="keypoint",
                ),
                dmc.Card(
                    [
                        dmc.Text("Maximum", size="xs"),
                        dmc.Text(id="max_nb_text" ,children=f"{max_value}", size="xl"),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    padding="md",
                    className="keypoint",
                ),
            ],
            gap="lg",
            grow=True,
            style={"width": "100%"},
            id=id,
        )
    else:
        return dmc.Text("No data available")

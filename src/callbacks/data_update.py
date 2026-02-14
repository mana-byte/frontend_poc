from dash import callback, Output, Input
from utils import fetch_data_from_api_by_date, get_max_from_data
import os

API_URL = os.getenv("API_URL", "http://localhost:6942/")
API_ROUTE_BY_DAY = os.getenv("API_ROUTE", "people_per_hour")


# FEtCH DATA CALLBACKS
@callback(
    Output("data-store", "data"),
    Input("mini-calendar", "value"),
)
def calendar_update(date: str):
    """Fetches data from the API based on the selected date from the mini-calendar and updates the data store
    Args:
        date (str): The selected date from the mini-calendar in the format "YYYY-MM-DD"
    Returns:
        dict: The data fetched from the API for the selected date
    """
    data = fetch_data_from_api_by_date(API_URL + API_ROUTE_BY_DAY, date)[::-1]
    data.append({"date": date})
    return data


# DATA UPDATE CALLBACKS
@callback(
    Output("linechart", "data"),
    Input("data-store", "data"),
)
def update_visualization(data):
    """Updates the line chart visualization based on the data stored in the data store"""
    return data


@callback(
    Output("current_nb_text", "children"),
    Input("data-store", "data"),
)
def update_current_nb_keypoint(data):
    """Updates the line chart visualization based on the data stored in the data store"""
    # -1 is the date, -2 is the latest data point
    return data[-2:][0]["nb_people"] if len(data) > 1 else "No data"


@callback(
    Output("max_nb_text", "children"),
    Input("data-store", "data"),
)
def update_max_nb_keypoint(data):
    """Updates the line chart visualization based on the data stored in the data store"""
    return get_max_from_data(data, "nb_people") if len(data) > 1 else "No data"

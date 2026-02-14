from dash import Dash, callback, Output, Input, dcc
from utils import fetch_data_from_api, fetch_data_from_api_by_date
import os

API_URL = os.getenv("API_URL", "http://localhost:6942/")
API_ROUTE_BY_DAY = os.getenv("API_ROUTE", "people_per_hour")

@callback(
    Output("data-store", "data"),
    Input("mini-calendar", "value"),
)
def calendar_update(date: str):
    data = fetch_data_from_api_by_date(API_URL + API_ROUTE_BY_DAY, date)
    print(data)
    return data


@callback(
    Output("linechart", "data"),
    Input("data-store", "data"),
)
def update_visualization(data):
    return data

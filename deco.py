import requests
import os
from datetime import datetime, date, timedelta

USERNAME = os.environ["DECO_USER"]
PASSWORD = os.environ["DECO_PASS"]
API_URL = "https://straighttohell.eu/api/json/manage_orders/find"


def get_weekly_priorities():
    """Return a list of priorities for the current week

    Retrieve the data of the orders from Deco API
    """

    first_day, last_day = get_days()

    first_day_formatted = first_day.strftime("%Y-%m-%dT00:00:00")
    last_day_formatted = last_day.strftime("%Y-%m-%dT00:00:00")

    params = {
        "field": "5",
        "condition": "7",
        "date1": first_day_formatted,
        "date2": last_day_formatted,
        "sortby": 5,
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.get(API_URL, params=params)
    priorities = get_priorities(response.json())

    return priorities


def get_days():
    """Return the starting end ending days of the current week"""
    first_day = datetime.today()

    last_day = first_day + timedelta(7)

    return first_day, last_day


def get_priorities(json_response):
    """"""
    priorities = []

    for order in json_response["orders"]:
        if order["is_priority"] and order["order_status"] != 7 and order["order_status"] != 4:
            priorities.append(order)

    return priorities

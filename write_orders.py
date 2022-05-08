import os
from datetime import date
DESKTOP_PATH = os.path.join(os.path.join(os.path.expanduser('~')), 'Scrivania')
FILE_PATH = DESKTOP_PATH + "/priorities.txt"

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []

days = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
days_name = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]


def format_days(orders):
    for order in orders:
        due_date = order["date_due"]
        due_year = due_date[0:4]
        due_month = due_date[5:7]
        due_day = due_date[8:10]

        week_day = date(int(due_year), int(due_month), int(due_day)).weekday()
        days[week_day].append(order)


def dump_orders(orders):
    format_days(orders)

    with open(FILE_PATH, "w") as f:
        for index, day in enumerate(days):
            if len(day) > 0:
                f.write(f"{days_name[index]}\n")
                f.write("----------------\n")
                for order in day:
                    billing_details = order["billing_details"]
                    if billing_details["company"] != "":
                        customer_name = billing_details["company"]
                    else:
                        customer_name = f"{billing_details['firstname']} {billing_details['lastname']}"

                    if order["job_name"] == "":
                        job_name = customer_name
                    else:
                        job_name = order["job_name"]

                    item_name = f"{order['order_id']} - {customer_name} - {job_name}"
                    f.write(f"Ordine {item_name}\n")
                f.write("\n\n")

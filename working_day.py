from datetime import date
days_name = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]


class WorkingDay:
    def __init__(self, workingday):
        self.date = workingday
        self.orders = []

    def get_day(self):
        week_day = days_name[self.date.weekday()]
        return f"{week_day} {self.date.day}\n"

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def has_orders(self):
        return len(self.orders) > 0

    def check_date(self, order_date):
        return self.date == order_date

    def get_date(self):
        return self.date

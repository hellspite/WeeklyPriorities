import deco
import write_orders

if __name__ == "__main__":
    orders = deco.get_weekly_priorities()
    # for order in orders:
    #     print(order["date_due"])
    write_orders.dump_orders(orders)

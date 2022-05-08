import deco
import write_orders

if __name__ == "__main__":
    orders = deco.get_weekly_priorities()
    write_orders.dump_orders(orders)

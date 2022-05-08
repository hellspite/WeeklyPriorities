import deco

if __name__ == "__main__":
    orders = deco.get_weekly_priorities()
    for order in orders:
        print(f"- Order: {order['order_id']}")

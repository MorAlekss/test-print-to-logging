def create_order(user_id, items):
    print(f"Creating order for user: {user_id}")
    if not items:
        print("ERROR: No items in order")
        return None
    order = {"id": 1, "user_id": user_id, "items": items}
    print(f"Order created: {order}")
    return order


def cancel_order(order_id):
    print(f"Cancelling order: {order_id}")
    print(f"Order {order_id} cancelled successfully")
    return True


def get_order_status(order_id):
    print(f"Fetching status for order: {order_id}")
    status = "pending"
    print(f"Order {order_id} status: {status}")
    return status

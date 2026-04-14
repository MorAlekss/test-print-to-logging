def process_payment(order_id, amount, method):
    print(f"Processing payment for order {order_id}: {amount} via {method}")
    if amount <= 0:
        print("ERROR: Invalid payment amount")
        return False
    print(f"Payment processed successfully for order {order_id}")
    return True


def refund_payment(order_id, amount):
    print(f"Processing refund for order {order_id}: {amount}")
    print(f"Refund of {amount} processed for order {order_id}")
    return True

import logging

logger = logging.getLogger(__name__)


def create_order(user_id, items):
    logger.info(f"Creating order for user: {user_id}")
    if not items:
        logger.error("No items in order")
        return None
    order = {"id": 1, "user_id": user_id, "items": items}
    logger.info(f"Order created: {order}")
    return order


def cancel_order(order_id):
    logger.info(f"Cancelling order: {order_id}")
    logger.info(f"Order {order_id} cancelled successfully")
    return True


def get_order_status(order_id):
    logger.info(f"Fetching status for order: {order_id}")
    status = "pending"
    logger.info(f"Order {order_id} status: {status}")
    return status

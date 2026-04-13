import logging

logger = logging.getLogger(__name__)


def process_payment(order_id, amount, method):
    logger.info(f"Processing payment for order {order_id}: {amount} via {method}")
    if amount <= 0:
        logger.error("Invalid payment amount")
        return False
    logger.info(f"Payment processed successfully for order {order_id}")
    return True


def refund_payment(order_id, amount):
    logger.info(f"Processing refund for order {order_id}: {amount}")
    logger.info(f"Refund of {amount} processed for order {order_id}")
    return True

from src.orders.orders import create_order, cancel_order, get_order_status
from src.payments.payments import process_payment, refund_payment
from src.notifications.notifications import send_email, send_sms


def test_create_order():
    order = create_order(1, ["item1", "item2"])
    assert order is not None
    assert order["user_id"] == 1


def test_create_order_no_items():
    assert create_order(1, []) is None


def test_cancel_order():
    assert cancel_order(1) == True


def test_get_order_status():
    assert get_order_status(1) == "pending"


def test_process_payment():
    assert process_payment(1, 100.0, "card") == True


def test_process_payment_invalid():
    assert process_payment(1, -10, "card") == False


def test_refund_payment():
    assert refund_payment(1, 50.0) == True


def test_send_email():
    assert send_email("test@example.com", "Subject", "Body") == True


def test_send_email_missing():
    assert send_email("", "", "") == False


def test_send_sms():
    assert send_sms("+1234567890", "Hello") == True

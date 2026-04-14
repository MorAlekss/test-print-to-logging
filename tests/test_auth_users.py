from src.auth.login import login, logout
from src.users.users import create_user, delete_user, update_user


def test_login_success():
    assert login("admin", "secret") == True


def test_login_failure():
    assert login("user", "wrong") == False


def test_login_missing_credentials():
    assert login("", "") == False


def test_create_user():
    user = create_user("john", "john@example.com")
    assert user is not None
    assert user["username"] == "john"


def test_delete_user():
    assert delete_user(1) == True


def test_update_user():
    assert update_user(1, {"email": "new@example.com"}) == True


def test_update_user_no_data():
    assert update_user(1, {}) == False

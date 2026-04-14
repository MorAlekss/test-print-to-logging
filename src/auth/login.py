def login(username, password):
    print(f"Login attempt for user: {username}")
    if not username or not password:
        print("ERROR: Missing credentials")
        return False
    if username == "admin" and password == "secret":
        print(f"Login successful for user: {username}")
        return True
    print(f"Login failed for user: {username}")
    return False


def logout(username):
    print(f"User {username} logged out")

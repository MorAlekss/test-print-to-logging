def create_user(username, email):
    print(f"Creating user: {username}, email: {email}")
    if not username or not email:
        print("ERROR: Missing required fields")
        return None
    user = {"id": 1, "username": username, "email": email}
    print(f"User created successfully: {user}")
    return user


def delete_user(user_id):
    print(f"Deleting user with id: {user_id}")
    print(f"User {user_id} deleted successfully")
    return True


def update_user(user_id, data):
    print(f"Updating user {user_id} with data: {data}")
    if not data:
        print("WARNING: No data provided for update")
        return False
    print(f"User {user_id} updated successfully")
    return True

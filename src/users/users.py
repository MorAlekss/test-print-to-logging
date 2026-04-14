import logging

logger = logging.getLogger(__name__)


def create_user(username, email):
    logger.info(f"Creating user: {username}, email: {email}")
    if not username or not email:
        logger.error("Missing required fields")
        return None
    user = {"id": 1, "username": username, "email": email}
    logger.info(f"User created successfully: {user}")
    return user


def delete_user(user_id):
    logger.info(f"Deleting user with id: {user_id}")
    logger.info(f"User {user_id} deleted successfully")
    return True


def update_user(user_id, data):
    logger.info(f"Updating user {user_id} with data: {data}")
    if not data:
        logger.warning("No data provided for update")
        return False
    logger.info(f"User {user_id} updated successfully")
    return True

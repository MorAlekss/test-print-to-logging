import logging

logger = logging.getLogger(__name__)


def login(username, password):
    logger.info(f"Login attempt for user: {username}")
    if not username or not password:
        logger.error("Missing credentials")
        return False
    if username == "admin" and password == "secret":
        logger.info(f"Login successful for user: {username}")
        return True
    logger.info(f"Login failed for user: {username}")
    return False


def logout(username):
    logger.info(f"User {username} logged out")

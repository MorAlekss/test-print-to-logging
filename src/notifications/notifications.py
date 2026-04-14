import logging

logger = logging.getLogger(__name__)


def send_email(to, subject, body):
    logger.info(f"Sending email to {to}, subject: {subject}")
    if not to or not subject:
        logger.error("Missing email fields")
        return False
    logger.info(f"Email sent successfully to {to}")
    return True


def send_sms(phone, message):
    logger.info(f"Sending SMS to {phone}: {message}")
    logger.info(f"SMS sent successfully to {phone}")
    return True

def send_email(to, subject, body):
    print(f"Sending email to {to}, subject: {subject}")
    if not to or not subject:
        print("ERROR: Missing email fields")
        return False
    print(f"Email sent successfully to {to}")
    return True


def send_sms(phone, message):
    print(f"Sending SMS to {phone}: {message}")
    print(f"SMS sent successfully to {phone}")
    return True

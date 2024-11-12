import smtplib
from email.mime.text import MIMEText

class Notification:
    def __init__(self, config):
        self.config = config

    def send_email_notification(self, recipient, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = "no-reply@organization.com"
        msg['To'] = recipient

        with smtplib.SMTP('smtp.organization.com') as server:
            server.login("user", "password")
            server.sendmail("no-reply@organization.com", recipient, msg.as_string())

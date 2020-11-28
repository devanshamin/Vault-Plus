import json
import smtplib
from typing import Text
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from utils.logger import logger

def email_otp(otp: Text, receiver_email: Text) -> None:
    """Send an email containing the OTP.
    
    Args:
        otp: One Time Password.
        receiver_email: Receiver's email address.
    """

    try:
        config = json.loads(Path("config.json").read_text())
        sender_email = config["email"]
        password = config["password"]
    except:
        raise Exception("Please enter your email and password in 'config.json'. Note: Email and password are required to send an OTP via email for 2FA.")

    message = MIMEMultipart()
    message['Subject'] = "One Time Password (OTP)"
    message['From'] = sender_email
    message['To'] = receiver_email
    html = """\
        <html>
        <body>
        <p><font size="15"> Your code is <b>{}</b> </font</p>
        </body>
        </html>
        """.format(otp)
    part = MIMEText(html, "html")
    message.attach(part)
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(sender_email, password)
        text = message.as_string()
        s.sendmail(sender_email, receiver_email, text)
        s.quit()
    except:
        logger.error("Error happened while sending an email!", exc_info=True)
import json
import smtplib
from typing import Text
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from utils.logger import logger

def email_code(code: Text, receiver_email: Text) -> None:
    """Send an email containing the random code.
    
    Args:
        code: A random 9-digit code.
        receiver_email: Receiver's email address.
    """

    e = "Please enter your email address and password in 'config.json'. Note: Email address and password are required to send an OTP via email for online 2FA."
    try:
        config = json.loads(Path("config.json").read_text())
        sender_email = config["email"]
        password = config["password"]
    except:
        raise Exception(e)
    
    if not sender_email or not password:
        raise Exception(e)

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
        """.format(code)
    part = MIMEText(html, "html")
    message.attach(part)
    try:
        # Note: 587 smtp port worked for me. If it doesn't work for you, 
        # you will have to tweak the smtp port to get yours to work.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(sender_email, password)
        text = message.as_string()
        s.sendmail(sender_email, receiver_email, text)
        s.quit()
    except:
        logger.error("Error happened while sending an email!", exc_info=True)
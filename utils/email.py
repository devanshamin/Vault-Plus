from typing import Text

import ezgmail

from utils.logger import logger

def email_otp(otp: Text, receiver_email: Text) -> None:
    """Send an email containing the OTP.
    
    Args:
        otp: One Time Password.
        receiver_email: Receiver's email address.
    """

    html = """\
        <p><font size="10"> Your OTP is <b style="color:blue;">{}</b> </font</p>
        """.format(otp)
    try:
        ezgmail.send(receiver_email, "One Time Password (OTP)", html, mimeSubtype='html')
    except:
        logger.error("Error happened while sending an email!", exc_info=True)
import string
from typing import Text

def id_(email: Text) -> Text:
    """Generate a user id.
    
    Args:
        email: User's email address.
    Returns:
        User id.
    """

    username, domain_name = email.split("@")
    domain_name = domain_name.split('.')[0]
    for char in string.punctuation:
        username = username.replace(char, "")
    return f"_{username}{domain_name}"
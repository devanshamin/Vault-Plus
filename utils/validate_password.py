import re
from typing import Text, Any

def pvalidate(pwd: Text) -> Any:
    """Validate the user's password.
    
    Args:
        pwd: User's password.
    Returns:
        None if password is valid else the problem.
    """
    if len(pwd) < 8:
        prb = "Make sure your password is at least 8 letters"
    elif re.search('[0-9]',pwd) is None:
        prb = "Make sure your password has a number in it"
    elif re.search('[A-Z]',pwd) is None: 
        prb = "Make sure your password has a uppercase letter in it"
    elif re.search('[a-z]',pwd) is None: 
        prb = "Make sure your password has a lowercase letter in it"
    else:
        prb = None
    return prb
import time
import threading
from ast import literal_eval
from typing import Text, List

from utils.logger import logger
from utils.email import email_otp
from utils.sequence import generate_otp, derive_code

code = ''
tflag = True
start_time = time.time() + 5
secondary_t1, secondary_t2 = 0, 0

def counter(sequence: Text, user_email: Text) -> None:
    """Send a new otp via email every 60 seconds.

    Args:
        sequence: User's sequence fetched from the database.
        user_email: User's email address.
    """
    global code
    sequence = literal_eval(sequence)
    length = [len(s.split(' | ')) for s in sequence]
    while tflag:
        otp = generate_otp(length)
        code = derive_code(otp, sequence)
        email_otp(otp, user_email)
        start = time.time()
        elapsed = 0
        seconds = 60
        while elapsed < seconds and tflag == True:
            elapsed = time.time() - start
            time.sleep(1)

def verify(user_code: Text) -> bool:
    """Verify the user code with the actual code.
    
    Args:
        user_code: Code entered by user for 2FA.
    Returns:
        True if the code matches else False.
    """
    global tflag
    if user_code != "Initial":
        while tflag:
            if user_code == code:
                tflag = False
                return True
            else:
                return False

def stop_execution():
    """Finish the execution of the threads by setting the flag to False."""
    global tflag
    tflag = False

def thread_1(sequence: Text, user_email: Text) -> None:
    """Create and start one thread.
    
    Args:
        sequence: User's sequence fetched from the database.
        user_email: User's email address.
    """
    global secondary_t1
    try:
        while time.time() <= start_time:
            pass
        secondary_t1 = threading.Thread(target = counter, args = (sequence, user_email,))
        secondary_t1.start()
    except:
        logger.error("Error occurred during execution of threads!", exc_info=True)

def thread_2(user_code: Text) -> None:
    """Create and start one thread.
    
    Args:
        user_code: Code entered by user for 2FA.
    """
    global secondary_t2
    try:
        while time.time() <= start_time:
            pass
        secondary_t2 = threading.Thread(target = verify, args=[user_code])
        secondary_t2.start()
    except:
        logger.error("Error occurred during execution of threads!", exc_info=True)

def threads_start(sequence: Text, user_email: Text, user_code: Text) -> None:
    """Create 2 threads and start them at the same time.
    
    Args:
        sequence: User's sequence fetched from the database.
        user_email: User's email address.
        user_code: Code entered by user for 2FA.
    """
    
    main_t1 = threading.Thread(target = thread_1, args = (sequence, user_email))
    main_t2 = threading.Thread(target = thread_2, args = [user_code])
    
    main_t1.start()
    main_t2.start()
    
    main_t1.join()
    secondary_t1.join()
    
    main_t2.join()
    secondary_t2.join()
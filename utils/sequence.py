import string
import random
from pathlib import Path
from ast import literal_eval
from typing import Text, List

from utils.adminDB import conn
from utils.logger import logger
from utils.pdf import PDF, encrypt_pdf

def generate_otp(length: List[int]) -> Text:
    """Generate a random OTP based on the length of user's sequence.
    
    Args:
        length: List containing length of each part in the sequence.
    Returns:
        A OTP.
    """

    otp = []
    for part in length:
        part = list(range(part))
        random.shuffle(part)
        c = ''.join(map(str, [random.choice(part) for i in range(3)]))
        otp.append(c)
    return '-'.join(otp)

def derive_code(otp: Text, sequence: List[Text]) -> Text:
    """Derive the code using the OTP and sequence.
    
    Args:
        otp: One Time Password.
        sequence: User's sequence.
    Returns:
        A code. 
    """

    # Convert parts of the sequence from string to dictionary.
    dict_sequence = []
    for s in sequence:
        s = "{" + s.replace(" | ",",") + "}"
        dict_sequence.append(literal_eval(s))

    code = []
    pieces = otp.split('-')
    for i in range(len(pieces)):
        for c in pieces[i]:
            code.append(dict_sequence[i][int(c)]) 
    return ''.join(code)

def generate() -> List[Text]:
    """Generate a random sequence.
    
    Returns:
        A sequence
    """
    
    p = [10, 10, 6]
    random.shuffle(p)
    c = list(string.ascii_uppercase)
    random.shuffle(c)

    f = lambda x, y: dict(zip(list(range(x)), y))
    clean = lambda x: str(x).replace("{"," ").replace("}"," ").replace(',', ' | ')

    sequence = []
    sequence.append(clean(f(p[0], c[: p[0]])))
    sequence.append(clean(f(p[1], c[p[0]: p[0]+p[1]])))
    sequence.append(clean(f(p[2], c[p[0]+p[1]:])))

    return sequence

def check(sequence: Text) -> bool:
    """Check if the sequence exists in the USERS table.
    
    Args:
        sequence: User's sequence.
    Returns:
        True if sequence exists in the database else False.
    """

    try:
        cursor = conn.execute("SELECT Sequence FROM USERS")
        db_seq = [r[0] for r in cursor]
        for seq in db_seq:
            if sequence == seq:
               return True
        return False
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def download_sequence(email: Text, mp: Text, sequence: Text, dir_path: Path) -> None:
    """Make, encrypt and save the user's sequence as a PDF file in users directory.
    
    Args:
        email: User's email address.
        mp: User's master password.
        sequence: User's sequence.
        dir_path: Directory path to save the PDF file.
    """

    pdf = PDF()
    pdf.set_title("Sequence")
    pdf.set_author("Vault Plus")
    pdf.add_page()
    pdf.print_chapter(1, sequence[0])
    pdf.print_chapter(2, sequence[1])
    pdf.print_chapter(3, sequence[2])
    pdf_name = "Unencrypted_Sequence.pdf"
    pdf.output(Path(dir_path, pdf_name), "F")
    encrypt_pdf(mp, Path(dir_path, pdf_name))
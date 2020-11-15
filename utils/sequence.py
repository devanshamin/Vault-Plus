import ast
import string
import random
from pathlib import Path
from typing import Text, List

from utils.logger import logger
from utils.adminDB import conn

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
        dict_sequence.append(ast.literal_eval(s))

    code = []
    pieces = otp.split('-')
    for i in range(len(pieces)):
        for c in pieces[i]:
            code.append(dict_sequence[i][int(c)]) 
    return ''.join(code)

def clean(dicto):
    return str(dicto).replace("{"," ").replace("}"," ").replace(',', ' | ')

def main():
    sequence = []
    
    alphabets = list(string.ascii_uppercase)
    part = [10, 10, 6]
    random.shuffle(part)
    random.shuffle(alphabets)
    
    sequence.append(clean(dict(zip(list(range(0,part[0])),alphabets[:part[0]]))))
    sequence.append(clean(dict(zip(list(range(0,part[1])),alphabets[part[0]:part[0] + part[1]]))))
    sequence.append(clean(dict(zip(list(range(0,part[2])),alphabets[part[1]:part[1] + part[2]]))))
        
    return sequence, part

def check_sequence(sequence: Text) -> bool:
    """Check if the sequence exists in the USERS table.
    
    Args:
        sequence: User's sequence.
    """

    try:
        cursor = conn.execute("SELECT Sequence FROM USERS")
        db_seq = [r[0] for r in cursor]
        for seq in db_seq:
            if sequence == seq:
               return True
        return False
    except BaseException:
        logger.error("Error happened which executing a SQL query!", exc_info=True)



def Download_Sequence(sq_no, email, password):
    try:
        i=1
        s = sequence[sq_no]
        for o in s:
            if i == 1:
                a = o
            elif i == 2:
                b = o
            elif i == 3:
                c = o
            i +=1
        pdf = PDF()
        pdf.set_title(title)
        pdf.set_author('Vault Plus')
        pdf.add_page()
        pdf.print_chapter(1, a)
        pdf.print_chapter(2, b)
        pdf.print_chapter(3, c)
        pdf.output('Sequence.pdf', 'F')
        Encrypt_pdf(password, email)
        return 0
    except:
        return 101
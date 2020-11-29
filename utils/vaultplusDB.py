import random
from pathlib import Path
from typing import Text, List

import sqlite3

from utils.user_id import id_
from utils.logger import logger
from utils.encryption import hex_key, AES_encrypt, AES_decrypt

vp_path = Path("vaultplus")
if not vp_path.exists():
    vp_path.mkdir()
conn = sqlite3.connect(Path(vp_path, 'VaultPlus.db'))

def users_table() -> None:
    """Create a USERS table in the VaultPlus database."""

    conn.execute('''CREATE TABLE IF NOT EXISTS USERS
                    (Email TEXT PRIMARY KEY,
                     Password TEXT,                           
                     Sequence TEXT,                 
                     BackupCode TEXT,
                     Type TEXT);''')

def insert_user(email: Text, mp: Text, sequence: bytes, bcode: bytes, type_: bytes) -> None:
    """Insert a user into the USERS table.
    
    Args:
        email: User's email address.
        mp: User's hashed master password.
        sequence: User's sequence cipher.
        bcode: User's backupcodes cipher.
        type_: 2FA type (Online/Offline).
    """

    try:
        conn.execute('''INSERT INTO USERS VALUES (?,?,?,?,?)''',(email, mp, sequence, bcode, type_))
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def uid_table(uid: Text) -> None:
    """Create a table for each user in the VaultPlus database.

    Args:
        uid: User's id (table name).
    """

    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS {}
                        (Service TEXT PRIMARY KEY,
                         Password TEXT)'''.format(uid))
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def generate_backupcode() -> Text:
    """Generate a backup code for the user.
    
    Returns:
        A backup code.
    """
    
    bcode = ''
    num = list(range(0, 9))
    for _ in range(0,8):
        r = random.choice(num)
        bcode += str(r)
        num.remove(r)
    
    return bcode

def check_backupcode(code: Text) -> bool:
    """Check if the backup code exists in the USERS table.

    Args:
        code: User's backup code.
    Returns:
        True if code exists in the database else False.
    """
    try:
        cursor = conn.execute("SELECT BackupCode FROM USERS")
        plain = ''
        for row in cursor:
            plain = AES_decrypt(row[0])
        return code in plain.split('-')
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def verify_email(email: Text) -> bool:
    """Verify if user's email address exists in the database.
    
    Args:
        email: User's email address.
    Returns:
        Presence of email address in the database.
    """
    try:
        cursor = conn.execute(f'SELECT * FROM USERS WHERE Email ="{email}"')
        for r in cursor: 
            return True if r[0] else False
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
        return False

def validate_mp(email: Text, mp: Text) -> bool:
    """Validate if the master password entered by the user matches with the password in the database.
    
    Args:
        email: User's email address.
        mp: User's master password.
    Returns:
        True if password matches else False.
    """

    hashed_mp = hex_key(id_(email), mp)
    try:
        cursor = conn.execute(f'SELECT Password FROM USERS WHERE Email ="{email}"')
        for row in cursor:
            return hashed_mp == row[0]
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
        return False

def fetch_sequence(email: Text) -> Text:
    """Fetch the user's sequence from the database.
    
    Args:
        email: User's email address.
    Returns:
        The sequence.
    """
    try:
        cursor = conn.execute(f'SELECT Sequence FROM USERS WHERE Email ="{email}"')
        for row in cursor:
            seq_cipher = row[0]
        return AES_decrypt(seq_cipher)
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def validate_backupcode(email: Text, code: Text) -> bool:
    """Validate if the backup code entered by the user matches with the backup code in the database.
    
    Args:
        email: User's email address.
        code: User's backup code.
    Returns:
        True if code matches else False.
    """

    try:
        cursor = conn.execute(f'SELECT BackupCode FROM USERS WHERE Email="{email}"')
        for row in cursor:
            bcodes = AES_decrypt(row[0])
        bool_ = code in bcodes.split('-')
        if bool_:
            while True:
                new_code = generate_backupcode()
                if not check_backupcode(new_code):
                    updated_bcodes = bcodes.replace(code, new_code)
                    update_backupcode(email, AES_encrypt(updated_bcodes))
                    break
        return bool_
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def update_backupcode(email: Text, code: Text) -> None:
    """Update the backup codes of a user in the USERS table.

    Args:
        email: User's email address.
        code: User's backup code.
    """

    try:
        conn.execute("UPDATE USERS SET BackupCode=? WHERE Email=?", (code, email))
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def fetch_password(uid: Text) -> dict:
    """Fetch user's password for all services.
    
    Args:
        uid: User's id.
    Returns:
        User's passwords for each service.
    """

    try:
        cursor = conn.execute(f"SELECT Service, Password FROM {uid}")
        password = {}
        for row in cursor:
            password[row[0]] =  AES_decrypt(row[1])
        return password
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def check_service(uid: Text, service: Text) -> bool:
    """Check if a user's service exists in the database.
    
    Args:
        uid: User's id.
        service: Name of user's service.
    Returns:
        True if service exists else False.
    """

    res = None
    try:
        cursor = conn.execute(f"SELECT * FROM {uid} WHERE Service='{service}'")
        for r in cursor:
            res = r[0]
        return res is not None
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def store_password(uid: Text, service: Text, password: Text) -> None:
    """Store a user's password for a given service.

    Args:
        uid: User's id.
        service: Name of user's service.
        password: Password for a service.
    """

    try:
        conn.execute(f"INSERT INTO {uid} VALUES (?,?)", (service, AES_encrypt(password)))
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def update_password(uid: Text, service: Text, password: Text) -> None:
    """Update a user's password for a given service.

    Args:
        uid: User's id.
        service: Name of user's service.
        password: Password for a service.
    """

    try:
        conn.execute(f"UPDATE {uid} SET Password=? WHERE Service=?", (AES_encrypt(password), service))
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def delete_password(uid: Text, service: Text) -> None:
    """Update a user's password for a given service.

    Args:
        uid: User's id.
        service: Name of user's service.
    """

    try:
        conn.execute(f"DELETE FROM {uid} WHERE Service='{service}'")
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def fetch_backupcodes(email: Text) -> Text:
    """Fetch user's backup codes from the database. 
    
    Args:
        email: User's email address.
    Returns:
        User's backup codes.
    """
    try:
        cursor = conn.execute(f"SELECT BackupCode FROM USERS WHERE Email='{email}'")
        for row in cursor:
            return AES_decrypt(row[0])
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def fetch_2FA_type(email: Text) -> Text:
    """Fetch user's 2FA type from the database. 
    
    Args:
        email: User's email address.
    Returns:
        User's 2FA type.
    """
    try:
        cursor = conn.execute(f"SELECT Type FROM USERS WHERE Email='{email}'")
        for row in cursor:
            return AES_decrypt(row[0])
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def delete_user(email: Text) -> None:
    """Delete a user from the database.
    
    Args:
        email: User's email address.
    """

    try:
        conn.execute(f"DROP TABLE {id_(email)}")
        conn.commit()

        conn.execute(f"DELETE FROM USERS WHERE Email='{email}'")
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
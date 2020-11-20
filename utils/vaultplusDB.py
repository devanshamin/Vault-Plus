from pathlib import Path
from typing import Text, List

import sqlite3

from utils.user_id import id_
from utils.logger import logger
from utils.encryption import hex_key, AES_decrypt

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
                     BackupCode TEXT);''')

def insert_user(email, mp, sequence, bcode) -> None:
    """Insert a user into the USERS table.
    
    Args:
        email: User's email address.
        mp: User's hashed master password.
        sequence: User's sequence cipher.
        bcode: User's backupcodes cipher.
    """
    conn.execute('''INSERT INTO USERS VALUES (?,?,?,?)''',(email, mp, sequence, bcode))
    conn.commit()

def uid_table(uid: Text) -> None:
    """Create a table for each user in the VaultPlus database.

    Args:
        uid: User's id (table name).
    """
    conn.execute('''CREATE TABLE IF NOT EXISTS {}
                    (Service TEXT PRIMARY KEY,
                     Password TEXT)'''.format(uid))

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
    except:
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
    except:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
        return False

def fetch_sequence(email: Text) -> List[Text]:
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
    except:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
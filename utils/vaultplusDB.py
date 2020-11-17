from pathlib import Path
from typing import Text, List

import sqlite3

from utils.logger import logger
from utils.encryption import AES_decrypt

vp_path = Path(Path.cwd(), "vaultplus")
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
                     Password TEXT);'''.format(uid))

def check_backupcode(code: Text) -> bool:
    """Check if the backup code exists in the USERS table.

    Args:
        code: User's backup code.
    Returns:
        True if code exists in the database else False.
    """
    try:
        cursor = conn.execute("SELECT BackupCode FROM USERS")
        for row in cursor:
            plain = AES_decrypt(row[0])
        return code in plain.split('-')
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
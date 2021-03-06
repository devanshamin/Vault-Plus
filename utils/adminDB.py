from pathlib import Path
from typing import Text, List

import sqlite3

from utils.user_id import id_
from utils.logger import logger

admin_path = Path("admin")
if not admin_path.exists():
    admin_path.mkdir()
conn = sqlite3.connect(Path(admin_path, "Admin.db"))

def users_table() -> None:
    """Create a USERS table in admin database."""

    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS USERS
            (Sequence TEXT PRIMARY KEY, 
            User TEXT);
            ''')
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def insert_user(sequence: Text, uid: Text) -> None:
    """Insert a user into the USERS table.
    
    Args:
        sequence: User's sequence.
        uid: User's id.
    """

    try:
        conn.execute("INSERT INTO USERS VALUES (?,?)",(sequence, uid))
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)

def delete_user(email: Text) -> None:
    """Delete a user from the USERS table.
    
    Args:
        email: User's email address.
    """

    try:
        conn.execute(f"DELETE FROM USERS WHERE User='{id_(email)[1:]}'")
        conn.commit()
    except BaseException:
        logger.error("Error happened while executing a SQL query!", exc_info=True)
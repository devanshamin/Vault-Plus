from pathlib import Path
from typing import Text, List

import sqlite3

admin_path = Path("..", "admin")
if not admin_path.exists():
    admin_path.mkdir()
conn = sqlite3.connect(Path(admin_path, "Admin.db"))

def users_table() -> None:
    """Create a USERS table in admin database."""

    conn.execute('''
        CREATE TABLE IF NOT EXISTS USERS
        (Sequence TEXT PRIMARY KEY, 
        User TEXT);
        ''')  

def insert_user(sequence: Text, uid: Text) -> None:
    """Insert a user into the USERS table.
    
    Args:
        sequence: User's sequence.
        uid: User's id.
    """

    conn.execute("INSERT INTO USERS VALUES (?,?)",(sequence, uid))
    conn.commit()

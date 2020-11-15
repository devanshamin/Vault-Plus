from pathlib import Path
from typing import Text, List

import sqlite3

vp_path = Path("..", "vaultplus")
if not vp_path.exists():
    vp_path.mkdir()
conn = sqlite3.connect(Path(vp_path, 'VaultPlus.db'))

def users_table() -> None:
    """Create a USERS table in VaultPlus database."""

    conn.execute('''CREATE TABLE IF NOT EXISTS USERS
                    (Email TEXT PRIMARY KEY,
                     Password TEXT,                           
                     Sequence TEXT,                 
                     BackupCode TEXT);''')                          

def user_detail_table(uid):
    conn.execute('''CREATE TABLE IF NOT EXISTS {}
                    (Service TEXT PRIMARY KEY,
                     Password TEXT);'''.format(uid))

def insert_users(M_Pass_key, Email, Sequence, Code):
    conn.execute('''INSERT INTO USERS VALUES (?,?,?,?)''',(Email, M_Pass_key, Sequence, Code))
    conn.commit()

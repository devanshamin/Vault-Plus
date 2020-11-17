from typing import Text
from hashlib import sha256
from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

bs = AES.block_size

# Each user will have a unique admin password
admin_pass = "nO9s6MuFRzfZiP"

# Key used for encryption and decryption
secret_key = PBKDF2(admin_pass, get_random_bytes(16), 64, 1000)[:32]

# Initialization vector used for randomizing the output
IV = secret_key[8:bs+8]

# Cipher Block Chaining
mode = AES.MODE_CBC

def hex_key(uid: Text, mp: Text) -> Text:
    """Create a hexadecimal key using an object of sha256.
    
    Args:
        uid: User's id.
        mp: User's master password.
    Returns:
        A string object containing only hexadecimal digits.
    """

    key = sha256(mp.encode('utf-8') + admin_pass.encode('utf-8')).hexdigest()
    return sha256(uid.lower().encode('utf-8') + key.encode('utf-8')).hexdigest()[:40]

def AES_encrypt(content: Text) -> bytes:
    """Encrypt the content using AES256.
    
    Args:
        content: Text to encrypt.
    Returns:
        Bytes containing the encrypted content.
    """
    cipher = AES.new(secret_key, mode, IV)
    body = Padding.pad(content.encode('utf-8'), bs)
    return b64encode(cipher.encrypt(body))

def AES_decrypt(ciphertext: bytes) -> Text:
    """Decrypt the ciphertext using AES256.
    
    Args:
        ciphertext: Encrypted text.
    Returns:
        Plain text.
    """
    text = b64decode(ciphertext)
    cipher = AES.new(secret_key, mode, IV)
    return Padding.unpad(cipher.decrypt(text), bs).decode('utf-8')
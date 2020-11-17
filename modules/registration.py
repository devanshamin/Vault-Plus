import random
from pathlib import Path
from typing import Text, List

from utils.user_id import id_
from utils import adminDB, vaultplusDB
from utils.pdf import PDF, encrypt_pdf
from utils.sequence import generate, check
from utils.encryption import hex_key, AES_encrypt

class Registration(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.uid = id_(self.email)

        vaultplusDB.users_table()
        user_sequence = self.generate_sequence()
        vaultplusDB.uid_table(self.uid)
        
        hashed_mp = hex_key(self.uid, self.password) # Master password ready for db insertion
        sequence_cipher = AES_encrypt(user_sequence) # Sequence_no ready for db insertion
        bcode_cipher = AES_encrypt(self.backupcode())
        vaultplusDB.insert_user(self.email, hashed_mp, sequence_cipher, bcode_cipher)

    def generate_sequence(self) -> Text:
        """Generate a unique sequence for the user.
        
        Returns:
            User's sequence.
        """

        adminDB.users_table()

        while True:
            sequence = str(generate())
            if not check(sequence):
                adminDB.insert_user(sequence, self.uid[1:])
                break

        dir_name = self.uid[1:]
        if not Path("..", dir_name).exists():
            Path("..", dir_name).mkdir()

        pdf = PDF()
        pdf.set_title("Sequence")
        pdf.set_author("Vault Plus")
        pdf.add_page()
        pdf.print_chapter(1, sequence[0])
        pdf.print_chapter(2, sequence[1])
        pdf.print_chapter(3, sequence[2])
        pdf_name = "Unencrypted_Sequence.pdf"
        pdf.output(pdf_name, "F")
        encrypt_pdf(self.password, Path(dir_name, pdf_name))

        return sequence

    def backupcode(self) -> Text:
        """Generate backup codes for the user.
        
        Returns:
            Backup codes.
        """
        bcode = []
        counter = 0
        while counter < 3:
            code = ''
            num = list(range(0, 9))
            for _ in range(0,8):
                r = random.choice(num)
                code += str(r)
                num.remove(r)
            if not vaultplusDB.check_backupcode(code):
                bcode.append(str(code))
                counter += 1

        text = """Keep these backup codes somewhere safe but accessible.\n\n{}
                \nEach backup code can be used once. \nAfter use of each backup code, a new backup 
                code is automatically generated and is available in the password manager.
                """.format('\n'.join(bcode)) 
        Path(vaultplusDB.vp_path, f"Backup codes({self.uid}).txt").write_text(text)

        return '-'.join(bcode)
        
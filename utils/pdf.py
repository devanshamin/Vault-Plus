from pathlib import Path
from typing import Text

import PyPDF2
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        title = 'Sequence'
        self.set_font('Arial', 'B', 22)
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(w, 9, title, 1, 1, 'C', 1)
        self.ln(10)

    def chapter_title(self, num):
        self.set_font('Arial', '', 18)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, 'Part %d ' % (num), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, txt):
        self.set_font('Times', '', 16)
        self.multi_cell(0, 5, txt)
        self.ln()
        
    def print_chapter(self, num, txt):
        self.chapter_title(num)
        self.chapter_body(txt)

def encrypt_pdf(email: Text, password: Text) -> None:
    """Encrypts a pdf file.
    
    Args:
        email: User's email address.
        password: User's password.
    """

    username, domain_name = email.split("@")
    domain_name = domain_name.split('.')[0]
    dir_name = f'{username}_{domain_name}'
    if not Path("VaultPlus", dir_name).exists():
        Path("VaultPlus", dir_name).mkdir()
    
    pdfFile = open('Unencrypted_Sequence.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    
    name = '../Sequence' +'_' + email + '.pdf'
    Path("Sequence")
    resultPdf = open(name, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    pdfFile.close()
    Path("Sequence.pdf").unlink()

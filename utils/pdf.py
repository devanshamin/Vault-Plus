from pathlib import Path
from typing import Text

import PyPDF2
from fpdf import FPDF

class PDF(FPDF):
    """Generate a PDF file."""

    def header(self) -> None:
        """Header of the page."""

        title = "Sequence"
        self.set_font("Arial", "BU", 22)
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(220, 50, 50)
        self.cell(w=w, h=9, txt=title, border=0, ln=1, align="C", fill=1, link="https://rdcu.be/caQXq")
        self.ln(10)

    def chapter_title(self, num: int) -> None:
        """Title of the chapter.

        Args:
            num: Part no for the user's sequence.
        """

        self.set_font("Arial", "", 18)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, "Part %d " % (num), 0, 1, "L", 1)
        self.ln(4)

    def chapter_body(self, txt: Text) -> None:
        """Body of the chapter.

        Args:
            txt: User's sequence.
        """

        self.set_font("Times", "", 16)
        self.multi_cell(0, 5, txt)
        self.ln()
        
    def print_chapter(self, num: int, txt: Text) -> None:
        """Write the chapter to the PDF file.

        Args:
            num: Part no for the user's sequence.
            txt: User's sequence.
        """

        self.chapter_title(num)
        self.chapter_body(txt)

def encrypt_pdf(password: Text, fpath: Path) -> None:
    """Encrypts a pdf file.
    
    Args:
        password: User's password.
        fpath: File path.
    """
    
    pdfFile = Path(fpath).open("rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    
    resultPdf = Path(fpath.parent, "Sequence.pdf").open("wb")
    pdfWriter.write(resultPdf)
    resultPdf.close()
    pdfFile.close()
    Path(fpath).unlink()
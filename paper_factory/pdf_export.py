import os
import win32com.client


def export_pdf(docx_path):
    pdf_path = docx_path.replace(".docx", ".pdf")

    abs_docx = os.path.abspath(docx_path)
    abs_pdf = os.path.abspath(pdf_path)

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    try:
        doc = word.Documents.Open(abs_docx)
        doc.SaveAs(abs_pdf, FileFormat=17)  # 17 = PDF
        doc.Close()
        return pdf_path

    finally:
        word.Quit()
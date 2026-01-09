from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import tempfile


def extract_text(file):
    suffix = file.filename.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(file.file.read())
        temp_path = tmp.name

    if suffix == "pdf":
        return extract_pdf_text(temp_path)

    if suffix == "docx":
        doc = Document(temp_path)
        return "\n".join(p.text for p in doc.paragraphs)

    return ""

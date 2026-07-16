from pathlib import Path

import pdfplumber
from docx import Document


class ResumeParser:

    @staticmethod
    def extract_text(file_path: str) -> str:

        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":
            return ResumeParser._extract_pdf(file_path)

        if suffix == ".docx":
            return ResumeParser._extract_docx(file_path)

        return ""

    @staticmethod
    def _extract_pdf(file_path: str) -> str:

        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    @staticmethod
    def _extract_docx(file_path: str) -> str:

        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )
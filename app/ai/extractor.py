import re


class ResumeExtractor:

    @staticmethod
    def extract_email(text: str):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        return match.group() if match else None

    @staticmethod
    def extract_phone(text: str):

        match = re.search(
            r"\+?\d[\d\s\-]{7,15}",
            text,
        )

        return match.group() if match else None
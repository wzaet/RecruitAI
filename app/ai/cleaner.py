import re


class ResumeCleaner:

    @staticmethod
    def clean(text: str) -> str:

        text = re.sub(r"\r", "\n", text)

        text = re.sub(r"\n+", "\n", text)

        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()
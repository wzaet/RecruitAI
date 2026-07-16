from app.ai.providers.base import AIProvider


class ResumeAnalyzer:

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def analyze(self, text: str):
        return self.provider.analyze_resume(text)

    def match(
        self,
        resume_text: str,
        job_description: str
    ):
        return self.provider.match_job(
            resume_text,
            job_description
        )
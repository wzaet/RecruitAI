from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def analyze_resume(self, text: str) -> dict:
        pass

    @abstractmethod
    def match_job(
        self,
        resume_text: str,
        job_description: str
    ) -> dict:
        pass
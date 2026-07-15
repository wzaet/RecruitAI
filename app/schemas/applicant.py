from pydantic import BaseModel


class ApplicantCreate(BaseModel):
    full_name: str
    email: str
    phone: str
    resume_path: str
    job_id: int


class ApplicantUpdate(BaseModel):
    full_name: str
    email: str
    phone: str
    resume_path: str
    job_id: int
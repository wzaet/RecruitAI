from pydantic import BaseModel, EmailStr


class ApplicantCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    job_id: int


class ApplicantResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    resume_path: str | None = None

    class Config:
        from_attributes = True
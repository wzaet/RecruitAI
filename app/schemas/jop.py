from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    department: str | None = None
    location: str | None = None
    employment_type: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    experience: str | None = None
    education: str | None = None
    description: str | None = None
    deadline: str | None = None
    class JobUpdate(JobCreate):
    pass
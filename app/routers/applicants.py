from fastapi import APIRouter, UploadFile, File, Form

from app.services.applicant_service import (
    create_applicant,
    get_applicants,
    delete_applicant,
)

router = APIRouter(
    prefix="/applicants",
    tags=["Applicants"]
)


@router.post("/")
def add_applicant(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    job_id: int = Form(...),
    resume: UploadFile = File(...)
):
    return create_applicant(
        full_name=full_name,
        email=email,
        phone=phone,
        job_id=job_id,
        resume=resume
    )


@router.get("/")
def list_applicants():
    return get_applicants()


@router.delete("/{applicant_id}")
def remove_applicant(applicant_id: int):
    return delete_applicant(applicant_id)
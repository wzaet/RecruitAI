import os
import shutil

from fastapi import UploadFile

from app.database.session import SessionLocal
from app.models.applicant import Applicant

UPLOAD_DIR = "uploads/resumes"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def create_applicant(
    full_name: str,
    email: str,
    phone: str,
    job_id: int,
    resume: UploadFile
):
    db = SessionLocal()

    try:
        file_path = os.path.join(
            UPLOAD_DIR,
            resume.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                resume.file,
                buffer
            )

        applicant = Applicant(
            full_name=full_name,
            email=email,
            phone=phone,
            job_id=job_id,
            resume_path=file_path
        )

        db.add(applicant)
        db.commit()
        db.refresh(applicant)

        return applicant

    finally:
        db.close()


def get_applicants():
    db = SessionLocal()

    try:
        return db.query(Applicant).all()

    finally:
        db.close()


def delete_applicant(applicant_id: int):
    db = SessionLocal()

    try:
        applicant = (
            db.query(Applicant)
            .filter(Applicant.id == applicant_id)
            .first()
        )

        if not applicant:
            return {"error": "Applicant not found"}

        if applicant.resume_path and os.path.exists(applicant.resume_path):
            os.remove(applicant.resume_path)

        db.delete(applicant)
        db.commit()

        return {"message": "Applicant deleted successfully"}

    finally:
        db.close()
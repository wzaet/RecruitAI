from app.database.session import SessionLocal
from app.models.applicant import Applicant
from app.schemas.applicant import ApplicantCreate, ApplicantUpdate


def create_applicant(applicant: ApplicantCreate):
    db = SessionLocal()

    try:
        new_applicant = Applicant(
            full_name=applicant.full_name,
            email=applicant.email,
            phone=applicant.phone,
            resume_path=applicant.resume_path,
            job_id=applicant.job_id,
        )

        db.add(new_applicant)
        db.commit()
        db.refresh(new_applicant)

        return {
            "id": new_applicant.id,
            "message": "Applicant created successfully",
        }

    finally:
        db.close()
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.certificate import (
    CertificateCreate,
    CertificateResponse,
    CertificateUpdate,
)
from app.services.certificate_service import certificate_service

router = APIRouter(
    prefix="/certificates",
    tags=["Certificates"],
)


@router.get("/{certificate_id}", response_model=CertificateResponse)
def get_certificate(
    certificate_id: int,
    db: Session = Depends(get_db),
):
    certificate = certificate_service.get(db=db, obj_id=certificate_id)

    if certificate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found",
        )

    return certificate


@router.post(
    "/",
    response_model=CertificateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_certificate(
    certificate_data: CertificateCreate,
    db: Session = Depends(get_db),
):
    return certificate_service.create_certificate(
        db=db,
        certificate_data=certificate_data,
    )


@router.put("/{certificate_id}", response_model=CertificateResponse)
def update_certificate(
    certificate_id: int,
    certificate_data: CertificateUpdate,
    db: Session = Depends(get_db),
):
    certificate = certificate_service.get(db=db, obj_id=certificate_id)

    if certificate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found",
        )

    return certificate_service.update_certificate(
        db=db,
        certificate=certificate,
        certificate_data=certificate_data,
    )


@router.delete(
    "/{certificate_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_certificate(
    certificate_id: int,
    db: Session = Depends(get_db),
):
    certificate = certificate_service.get(db=db, obj_id=certificate_id)

    if certificate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found",
        )

    certificate_service.delete(db=db, obj=certificate)
from fastapi import FastAPI

from app.api.company import router as company_router
from app.api.jobs import router as jobs_router
from app.api.users import router as users_router


def register_routers(app: FastAPI) -> None:
    app.include_router(users_router)
    app.include_router(jobs_router)
    app.include_router(company_router)
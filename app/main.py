from fastapi import FastAPI

from app.api.router import api_router
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="WZAET API",
    version="1.0.0",
    description="AI-powered recruitment platform for WZAET",
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to WZAET API",
        "status": "running",
    }
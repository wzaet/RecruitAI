from fastapi import APIRouter

from app.routers import (
    applications_router,
    auth_router,
    awards_router,
    certificates_router,
    companies_router,
    company_members_router,
    educations_router,
    experiences_router,
    jobs_router,
    languages_router,
    projects_router,
    references_router,
    resume_links_router,
    resume_skills_router,
    resumes_router,
    skills_router,
    users_router,
)

api_router = APIRouter()

# Authentication
api_router.include_router(auth_router)

# Users & Companies
api_router.include_router(users_router)
api_router.include_router(companies_router)
api_router.include_router(company_members_router)

# Jobs & Applications
api_router.include_router(jobs_router)
api_router.include_router(applications_router)

# Resume
api_router.include_router(resumes_router)
api_router.include_router(experiences_router)
api_router.include_router(educations_router)
api_router.include_router(projects_router)
api_router.include_router(certificates_router)
api_router.include_router(awards_router)
api_router.include_router(languages_router)
api_router.include_router(references_router)
api_router.include_router(resume_links_router)
api_router.include_router(resume_skills_router)
api_router.include_router(skills_router)
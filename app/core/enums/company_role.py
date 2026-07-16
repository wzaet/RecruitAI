from enum import Enum

class CompanyRole(str, Enum):

    COMPANY_ADMIN = "company_admin"

    RECRUITER = "recruiter"

    HIRING_MANAGER = "hiring_manager"
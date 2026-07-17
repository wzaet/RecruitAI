from enum import Enum


class EmploymentType(str, Enum):
    """
    Represents the type of employment for a work experience.
    """

    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    TEMPORARY = "TEMPORARY"
    FREELANCE = "FREELANCE"
    INTERNSHIP = "INTERNSHIP"
    APPRENTICESHIP = "APPRENTICESHIP"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    VOLUNTEER = "VOLUNTEER"
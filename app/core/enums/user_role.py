from enum import Enum


class UserRole(str, Enum):
    CANDIDATE = "candidate"
    PLATFORM_ADMIN = "platform_admin"
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==========================
    # Application
    # ==========================

    APP_NAME: str = "WZAET API"
    APP_VERSION: str = "1.0.0"

    # ==========================
    # Database
    # ==========================

    DATABASE_URL: str

    # ==========================
    # Security
    # ==========================

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
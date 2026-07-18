from pathlib import Path
import secrets

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DATABASE_NAME = "wzaet.db"
DATABASE_PATH = BASE_DIR / "data" / DATABASE_NAME

# JWT
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
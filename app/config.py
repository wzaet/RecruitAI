from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DATABASE_NAME = "recruitai.db"
DATABASE_PATH = BASE_DIR / "data" / DATABASE_NAME
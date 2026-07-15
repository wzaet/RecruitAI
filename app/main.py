from app.database.base import Base
from app.database.session import engine

# استيراد جميع النماذج
from app.models.job import Job


def main():
    Base.metadata.create_all(bind=engine)
    print("RecruitAI Started")
    print("Database Ready")


if __name__ == "__main__":
    main()
        
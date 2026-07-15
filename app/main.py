from database.database import Database

def main():
    print("=" * 40)
    print(" RecruitAI")
    print(" AI Recruitment Platform")
    print("=" * 40)

    db = Database()
    db.create_tables()
    db.close()

    print("✓ Database Ready")


if __name__ == "__main__":
    main()
        
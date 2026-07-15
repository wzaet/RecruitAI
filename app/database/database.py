import sqlite3
from pathlib import Path

from app.config import DATABASE_PATH

DB_NAME = DATABASE_PATH


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            department TEXT,
            location TEXT,
            employment_type TEXT,
            salary_min INTEGER,
            salary_max INTEGER,
            experience TEXT,
            education TEXT,
            description TEXT,
            deadline TEXT,
            status TEXT DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    db.close()
    print("Database created successfully.")
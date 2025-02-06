import sqlite3

class Database:
    """Manages the database connection and operations"""
    def __init__(self, db_path: str = "ai_system.db"):
        self.connection = sqlite3.connect(db_path)

    def close(self):
        """Close the database connection"""
        self.connection.close()
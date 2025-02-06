class UserProfile:
    """Manages user profiles and authentication"""
    def __init__(self, db: Database):
        self.db = db

    def authenticate(self, username: str, password: str) -> int:
        """Authenticate a user and return their user ID"""
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        return result[0] if result else None

    def create_profile(self, username: str, password: str):
        """Create a new user profile"""
        with self.db.connection:
            self.db.connection.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
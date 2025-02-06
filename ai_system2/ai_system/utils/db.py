import asyncio
import aiosqlite
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AsyncDatabase:
    """Asynchronous Database manager for user profiles and interaction logs"""
    def __init__(self, db_path: str = "ai_system.db"):
        self.db_path = db_path

    async def create_tables(self):
        """Create necessary tables in the database"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT
                )
            """)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    query TEXT,
                    response TEXT,
                    feedback TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            """)
            await db.commit()

    async def add_user(self, username: str, password: str):
        """Add a new user to the database"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            await db.commit()

    async def get_user(self, username: str) -> Optional[Dict]:
        """Retrieve user information from the database"""
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT * FROM users WHERE username = ?", (username,)) as cursor:
                return await cursor.fetchone()

    async def log_interaction(self, user_id: int, query: str, response: str, feedback: Optional[str] = None):
        """Log user interaction in the database"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("INSERT INTO interactions (user_id, query, response, feedback) VALUES (?, ?, ?, ?)", (user_id, query, response, feedback))
            await db.commit()

    async def close(self):
        """Close the database connection"""
        # No need to explicitly close the connection as it is managed by the context manager

# Example usage
async def main():
    db = AsyncDatabase()
    await db.create_tables()
    await db.add_user("test_user", "secure_password")
    user = await db.get_user("test_user")
    logger.info(f"Retrieved user: {user}")
    await db.log_interaction(user_id=user[0], query="What is the weather?", response="Sunny", feedback="Good")
    await db.close()

# Run the example
asyncio.run(main())

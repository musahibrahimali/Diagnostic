import sqlite3
from PySide2.QtCore import QObject


# database handler class
class DatabaseHandler(QObject):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    # create table
    def create_table(self):
        # the users should have a unique username, so we use the UNIQUE
        # keyword and a boolean with default as false for clinician
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (fullname TEXT, email TEXT UNIQUE, password TEXT, isClinician BOOLEAN DEFAULT 0)"
        )

    # register user
    def register_user(self, fullname: str, email: str, password: str, isClinician: bool = False):
        try:
            self.cursor.execute(
                "INSERT INTO users (fullname, email, password, isClinician) VALUES (?, ?, ?, ?)",
                (fullname, email, password, isClinician),
            )
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # check login
    def check_login(self, email: str):
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = self.cursor.fetchone()
        return user

    # login user
    def login_user(self, email: str, password: str):
        self.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cursor.fetchone()
        return user

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_email(self):
        user = User(email="user@example.com")
        self.assertEqual(user.email, "user@example.com")

if __name__ == "__main__":
    unittest.main()


import unittest
from dotenv import load_dotenv
import os


class TestEnv(unittest.TestCase):
    def setUp(self):
        load_dotenv()

    def test_username(self):
        username = os.getenv('INSTAGRAM_USER')
        self.assertNotEqual(username, '')

    def test_password(self):
        password = os.getenv('INSTAGRAM_PASSWORD')
        self.assertNotEqual(password, '')

    def test_nickname(self):
        nickname = os.getenv('INSTAGRAM_NICKNAME')
        self.assertNotEqual(nickname, '')
    
    def test_headless(self):
        headless = bool(os.getenv('HEADLESS', 'False').lower() in ('true', '1', 't'))
        self.assertFalse(headless)
    
    def test_login_save(self):
        login_save = bool(os.getenv('LOGIN_SAVE', 'False').lower() in ('true', '1', 't'))
        self.assertFalse(login_save)


if __name__ == "__name__":
    unittest.main()

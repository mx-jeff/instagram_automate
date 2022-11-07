import os
import unittest
from time import sleep

from scrapper_boilerplate import setSelenium, explicit_wait, generate_random_time
from src.instagram import Instagram
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


class TestBlock(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.driver = setSelenium(headless=False, remote_webdriver=True, profile=True)
        self.bot = Instagram(self.driver)
        self.bot.login(os.getenv('INSTAGRAM_USER'), os.getenv('INSTAGRAM_PASSWORD'))

    def test_block_user(self):
        # self.driver.get()
        status = self.bot.block('https://www.instagram.com/luigyzera/')
        self.assertTrue(status)
        isUnbloqued = self.bot.unblock('https://www.instagram.com/luigyzera/')
        self.assertTrue(isUnbloqued)
        # sleep(30)

    def tearDown(self) -> None:
        # return super().tearDown()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

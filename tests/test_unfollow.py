import os
import unittest
from time import sleep

from scrapper_boilerplate import setSelenium, explicit_wait, generate_random_time
from scrapper_boilerplate.output import log
from src.instagram import Instagram
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


def load_users():
    df = pd.read_csv('./followed.csv')
    urls = df['followed'].tolist()
    return urls


class TestUnfollow(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.driver = setSelenium(headless=False, remote_webdriver=True, profile=True)
        self.bot = Instagram(self.driver)
        self.bot.login(os.getenv('INSTAGRAM_USER'), os.getenv('INSTAGRAM_PASSWORD'))
        # self.users = load_users()

    def test_unfollow_user(self):
        self.driver.get('https://www.instagram.com/')
        generate_random_time(5, 10)
        
        # click on persoanl page 
        log('> clicando na página de perfil')
        # username = self.driver.find_element(By.CSS_SELECTOR, '._ab8w._ab94._ab99._ab9f._ab9k._ab9o._abb1._abcm a').get_attribute('href')
        # # log(username)
        # nickname = username.split('/')[3]
        self.bot.get_following()
        # select unfollow

    def tearDown(self) -> None:
        # return super().tearDown()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

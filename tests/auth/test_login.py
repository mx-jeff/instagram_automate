import unittest
import os
from dotenv import load_dotenv
from src.instagram.login import _login
from src.instagram.load import _load_page
from scrapper_boilerplate import setSelenium, explicit_wait
from scrapper_boilerplate.warnings import disable_warnings
from scrapper_boilerplate.setup import init_log

from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    def setUp(self):
        init_log()
        disable_warnings()
        load_dotenv()
        self.driver = setSelenium(remote_webdriver=True, headless=False)

    def test_login(self):
        _login(self.driver, os.getenv('INSTAGRAM_USER'), os.getenv('INSTAGRAM_PASSWORD'))
        suggestions = _load_page(self.driver, By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div')
        # print(suggestions.text)
        self.assertIsNotNone(suggestions)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

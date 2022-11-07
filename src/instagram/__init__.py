import logging
from time import sleep

from src.instagram.login import _login
from src.instagram.load import _load_page
from src.instagram.follow import _follow, _unfollow
from src.instagram.block import _block, _unblock

from selenium.webdriver.common.by import By
from scrapper_boilerplate import log


class Instagram:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        _login(self.driver, username, password)

    def load_page(self, element, selector_type="'/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div'"):
        _load_page(self.driver, element, selector_type)

    def search_profile(self, username):
        self.driver.get('https://www.instagram.com/' + username)
        
    def get_followers(self, profile):
        log("> Carregando página de seguidores...")
        self.driver.get('https://www.instagram.com/' + profile + '/followers/')
        _load_page(self.driver, By.CSS_SELECTOR, 'div._aae-')
        div = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        # scrolldown(self.driver, div)
        log("> Carregamento completo!")
        log("> Iniciando seguidores...")
        profiles = div.find_elements(By.CSS_SELECTOR, 'div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm')
        log(f"{len(profiles)} followers found!")

        _follow(profiles)       

    def get_following(self):
        username = self.driver.find_element(By.CSS_SELECTOR, '._ab8w._ab94._ab99._ab9f._ab9k._ab9o._abb1._abcm a').get_attribute('href')
        # log(username)
        nickname = username.split('/')[3]

        log("> Carregando página de seguidas...")
        self.driver.get('https://www.instagram.com/' + nickname + '/following/')
        _load_page(self.driver, By.CSS_SELECTOR, 'div._aae-')
        div = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        # scrolldown(self.driver, div)
        log("> Carregamento completo!")
        log("> Iniciando seguidas...")
        profiles = div.find_elements(By.CSS_SELECTOR, 'div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm')
        log(f"{len(profiles)} followers found!")

        _unfollow(profiles)


    def block(self, url:str):
        """
        blocks user

        args:
            - url: url of profile
        
        return:
            - status: True if successful!
        """
        self.driver.get(f"https://www.instagram.com/{url}")
        status = _block(self.driver)
        return status

    def unblock(self, url:str):
        """
        unblocks user if are blocked

        args:
            - url: url of profile
        
        return:
            - status: True if successful!
        """
        print("")
        self.driver.get(f"https://www.instagram.com/{url}")
        status = _unblock(self.driver)
        return status

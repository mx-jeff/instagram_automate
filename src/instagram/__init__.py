import logging
from time import sleep

from src.instagram.login import _login
from src.instagram.load import _load_page
from src.instagram.follow import _follow

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
        div = self.driver.find_element_by_css_selector('div._aano')
        # scrolldown(self.driver, div)
        log("> Carregamento completo!")
        log("> Iniciando seguidores...")
        profiles = div.find_elements_by_css_selector('li div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8')
        log(f"{len(profiles)} followers found!")

        _follow(profiles)        

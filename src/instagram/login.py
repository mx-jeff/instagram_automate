import sys
import logging
from time import sleep
from scrapper_boilerplate import explicit_wait, log
from selenium.webdriver.common.by import By


def _login(driver, username, password):
    log("> iniciando login...")

    login_url = 'https://www.instagram.com/accounts/login/'
    driver.get(login_url)
    
    if driver.current_url == 'https://www.instagram.com/': 
        log("> Atualmente ja está logado!")
        return 

    form = explicit_wait(driver, By.ID, 'loginForm') #self.driver.find_element_by_id('loginForm')
    
    form.find_element(By.NAME, 'username').send_keys(username)
    form.find_element(By.NAME, 'password').send_keys(password)
    form.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas').click()
    sleep(10)
    # driver.save_screenshot('login.png')
    if driver.current_url == login_url:
        log("> Erro ao realizar o login!")
        driver.quit()
        sys.exit()

    log("> Login realizado com sucesso!")
    return True

import os
import logging
import getpass

from src.instagram import Instagram
from src.utils import csvToList
from dotenv import load_dotenv
from scrapper_boilerplate.warnings import disable_warnings
from scrapper_boilerplate import setSelenium, explicit_wait, generate_random_time, log
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename='instagram.log', filemode='a')


def main():
    log("> iniciando...")
    disable_warnings()
    log("> desabilitando avisos...")
    load_dotenv()
    log("> carregando variaveis de ambiente...")

    user = os.getenv('INSTAGRAM_USER')
    password = os.getenv('INSTAGRAM_PASSWORD')
    headless = bool(os.getenv('HEADLESS', 'False').lower() in ('true', '1', 't'))
    nickname = csvToList('assets/profile_target.csv')[0] #os.getenv('INSTAGRAM_NICKNAME')
    login_save = bool(os.getenv('LOGIN_SAVE', 'False').lower() in ('true', '1', 't'))

    log("> carregamento completo!")

    with setSelenium(remote_webdriver=True, headless=headless, profile=login_save) as driver:
        try:
            driver.set_window_size(1280, 1024)
            instagram = Instagram(driver)
            instagram.login(user, password)
            instagram.load_page(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div')
            instagram.unblock(nickname)
            instagram.get_followers(nickname)
            generate_random_time(10, 10) #dinamic
            instagram.get_following()
            instagram.block(nickname)
    
        except Exception as err:
            driver.save_screenshot('error.png')
            logging.error(err)
            raise


if __name__ == "__main__":
    main()

import logging
from time import sleep

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from scrapper_boilerplate import generate_random_time, log, dataToCSV, explicit_wait
from selenium.webdriver.common.by import By

from src.utils import save_user


def _follow(profiles):
    for index, profile in enumerate(profiles):
        try:
            button = profile.find_element(By.CSS_SELECTOR,'button._acan._acap._acas')
            name = profile.find_element(By.CSS_SELECTOR, 'span._aap6._aap7._aap8').text
            url = profile.find_element(By.CSS_SELECTOR, 'a[role="link"]')

        except NoSuchElementException:
            log('Não disponível...\n')
            continue
        
        if button.text == 'Seguir':
            log(f"{index}/{len(profiles)} perfis")
            try:
                button.click()
            
            except ElementClickInterceptedException:
                log('limite alcançado!')
                sleep(60 * 10)
                _ok = profile.find_element(By.XPATH, '//div[text()="OK"]')
                _ok.click()

            log(f'Followed: {name}')
            save_user(url)
            generate_random_time(5, 10)                


def _unfollow(profiles):
    for index, profile in enumerate(profiles):
        try:
            button = profile.find_element(By.CSS_SELECTOR,'button[type="button"]')
            name = profile.find_element(By.CSS_SELECTOR, 'a[role="link"]').text
            url = profile.find_element(By.CSS_SELECTOR, 'a[role="link"]')

        except (NoSuchElementException, ElementClickInterceptedException) as error:
            log('Não disponível...\n')
            continue
        
        if button.text == 'Seguindo' and name != "zayvky":
            log(f"{index}/{len(profiles)} perfis")
            try:
                button.click()
                confirm = explicit_wait(profile, By.XPATH, '//button[text()="Deixar de seguir"]')
                confirm.click()
            
            except ElementClickInterceptedException:
                log('Um erro ocorreu ou o limite foi alcnçado')
                sleep(60 * 10)
                _ok = profile.find_element(By.XPATH, '//div[text()="OK"]')
                _ok.click()
            
            log(f'Parou de seguir: {name}')
            generate_random_time(5, 10)                


def _unfollow_by_link_name(driver, users):
    for index, user in enumerate(users):
        log(f"{index}/{len(users)} perfis")
        driver.get(user)

        log('> Deixando de seguir usário...')
        explicit_wait(driver, By.TAG_NAME, 'body')
        generate_random_time(5, 10)

        try:
            follow_btn = driver.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acat')[1]
            follow_btn.click()

            generate_random_time(3, 7)

            confirm_block = driver.find_element(By.XPATH, '//button[text()="Deixar de seguir"]')
            confirm_block.click()
            generate_random_time(3, 7)
            log('> Usuário deixado de seguir...')
            
        except (NoSuchElementException, IndexError):
            log('Erro de unfollow :(')

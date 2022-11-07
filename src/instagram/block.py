from scrapper_boilerplate import explicit_wait, generate_random_time
from scrapper_boilerplate.output import log
from selenium.webdriver.common.by import By
import logging


def _block(driver):
    explicit_wait(driver, By.TAG_NAME, 'body')
    # sleep(10)
    generate_random_time(5, 10)
    log('> Bloqueando usuário...')

    more_options = driver.find_elements(By.CSS_SELECTOR, 'button._abl-')[0]
    # print(more_options.get_attribute('outerHTML'))
    more_options.click()
    generate_random_time(3, 7)
    block = driver.find_element(By.XPATH, '//button[text()="Bloquear"]')
    block.click()
    
    generate_random_time(3, 7)
    confirm_block = driver.find_element(By.XPATH, '//button[text()="Bloquear"]')
    confirm_block.click()
    log('> Usuário bloqueado!')
    return True

def _unblock(driver):
    explicit_wait(driver, By.TAG_NAME, 'body')
    generate_random_time(5, 10)

    log('> Desbloqueado usuário...')
    unblock = driver.find_element(By.XPATH, '//div[text()="Desbloquear"]')
    unblock.click()
    
    generate_random_time(3, 7)
    confirm_unblock = driver.find_element(By.XPATH, '//button[text()="Desbloquear"]')
    confirm_unblock.click()
    generate_random_time(3, 7)

    ignore = driver.find_element(By.XPATH, '//button[text()="Ignorar"]')
    ignore.click()
    log('> Usuário desbloqueado!')
    generate_random_time(3, 7)
    return True

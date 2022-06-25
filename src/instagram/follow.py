import logging

from selenium.common.exceptions import NoSuchElementException
from scrapper_boilerplate import generate_random_time, log


def _follow(profiles):
    for profile in profiles:
        try:
            button = profile.find_element_by_css_selector('button._acan._acap._acas')

        except NoSuchElementException:
            log(profile.text)
            log('Não disponível...\n')
            continue
        
        if button.text == 'Seguir':
            button.click()
            log('Followed: ' + profile.text)
            generate_random_time(5, 10)                


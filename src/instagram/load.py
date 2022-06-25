from scrapper_boilerplate import explicit_wait


def _load_page(driver, selector_type, element):
    """
    Loads the page.
    
    args:
        driver: selenium webdriver
        selector_type: By.CSS_SELECTOR, By.XPATH, By.ID, By.CLASS_NAME
        element: selenium element

    """
    waiter = explicit_wait(driver, selector_type, element)
    
    waiter if waiter else False

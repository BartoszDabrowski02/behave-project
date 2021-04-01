from selenium.webdriver.common.by import By


def get_by_type(locator):
    locator_type = {
        'class': By.CLASS_NAME,
        'id' : By.ID,
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'link': By.LINK_TEXT,
    }
    return locator_type.get(locator.lower())


def get_element(context, locator_type, locator):
    by_type = get_by_type(locator_type)
    return context.driver.find_element(by_type, locator)

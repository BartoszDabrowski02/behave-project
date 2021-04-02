import time

from selenium.webdriver.common.by import By


def get_by_type(locator_type):
    locators = {
        "class": By.CLASS_NAME,
        "id": By.ID,
        "css": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "name": By.NAME,
        "link": By.LINK_TEXT,
    }
    return locators.get(locator_type.lower())


def get_element(context, locator_type, locator):
    by_type = get_by_type(locator_type)
    return context.driver.find_element(by_type, locator)


def get_elements(context, locator_type, locator):
    by_type = get_by_type(locator_type)
    return context.driver.find_elements(by_type, locator)


def send_keys_with_delay(element, text, delay=0.1):
    """Send a text to an element one character at a time with a delay."""
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

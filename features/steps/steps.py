import time

from behave import *
from selenium import webdriver


@given('we are present on google website')
def step_impl(context):
    # driver = webdriver.Chrome()
    # driver.get("https://www.google.pl/")
    pass


@given('we have generated order number')
def generate_order_number(context):
    context.order_number = '123456'


@then('our order number is...')
def then_order_number(context):
    print(context.order_number)


@when('we search for "{text}"')
def step_impl(context, text):
    print(f"We are searching for '{text}'")
    # time.sleep(3)
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    # try:
    #     button_one = driver.find_element_by_xpath(".//span[text()='Zgadzam się']")
    #     button_one.click()
    # except:
    #     pass
    # # text_box = driver.find_element_by_xpath(".//input[@aria-label='Szukaj']")
    # # search_button = driver.find_element_by_xpath(".//input[@aria-label='Szukaj w Google']")
    # # text_box.send_keys(text)
    # time.sleep(5)
    # search_button.click()


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False



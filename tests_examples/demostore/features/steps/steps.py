from behave import *
from selenium import webdriver


@given('we are present on home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://demostore.supersqa.com")


@then('page title is {text}')
def then_order_number(context, text):
    assert text == f'"{context.driver.title}"'

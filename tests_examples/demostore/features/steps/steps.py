from behave import *
from selenium import webdriver

# from tests_examples.base.common import navigate_to_page


@given('we are present on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.get("http://demostore.supersqa.com")


@when('we click on {tab_label} tab')
def then_order_number(context, tab_label):
    tab_label = tab_label.replace('"', '')
    tab_selector = context.driver.find_element_by_xpath(f".//ul[@class='nav-menu']//a[text()='{tab_label}']")
    tab_selector.click()


@then('the page title is {text}')
def then_order_number(context, text):
    assert text == f"{context.driver.title}"


@then('the {tab} tab is present')
def then_order_number(context, tab_label):
    tab_selector = context.driver.find_element_by_xpath(f".//ul[@class='nav-menu']//a[text()='{tab_label}']")
    tab_selector.is_displayed()

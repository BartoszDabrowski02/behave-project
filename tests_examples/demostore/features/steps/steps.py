import random

from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@given('we are present on the home page')
def go_to_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.get("http://demostore.supersqa.com")


@when('we click on {tab_label} tab')
def click_on_tab(context, tab_label: str):
    tab_selector = context.driver.find_element_by_xpath(f".//ul[@class='nav-menu']//a[text()='{tab_label}']")
    tab_selector.click()


@when('we add random item to the cart')
def add_random_item_to_the_cart(context):
    while True:
        random_item = random.randint(1, len(context.driver.find_elements_by_xpath("//ul[@class='products columns-4']/li")))
        context.item_name = context.driver.find_element_by_xpath(f"//ul[@class='products columns-4']/li[{random_item}]").text
        try:
            element = context.driver.find_element_by_xpath(f"//ul[@class ='products columns-4']/li[{random_item}]/a[text()='Add to cart']")
            context.elements_id = element.get_attribute('data-product_id')
            context.driver.find_element_by_xpath(f"//ul[@class ='products columns-4']/li[{random_item}]/a[text()='Add to cart']").click()
            break
        except NoSuchElementException:
            pass


@then('the page title is {text}')
def page_title(context, text: str):
    assert text == f"{context.driver.title}"


@then('the randomly selected item is in the cart')
def is_randomly_selected_item_in_the_cart(context):
    context.driver.find_element_by_xpath(f".//ul[contains(@class,'woocommerce-mini-cart')]//a[@data-product_id='{context.elements_id}']").is_displayed()


@then('the {tab_label} tab is present')
def tab_is_present(context, tab_label):
    tab_selector = context.driver.find_element_by_xpath(f".//ul[@class='nav-menu']//a[text()='{tab_label}']")
    tab_selector.is_displayed()


@then('there are {items_in_cart} items in the cart')
def number_of_items_in_the_cart(context, items_in_cart: str):
    items_in_cart_label = context.driver.find_element_by_css_selector("a.cart-contents span.count").text
    number_of_items = items_in_cart_label.split()[0]
    assert items_in_cart == number_of_items

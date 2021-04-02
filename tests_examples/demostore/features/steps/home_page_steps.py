import random

from behave import when, then
from selenium.common.exceptions import NoSuchElementException

from base.assertions import assert_element_is_visible, assert_element_is_present, assert_text_equal
from base.functions import get_element, get_elements
from locators.demostore_locators import NAVIGATION_BAR_LOCATORS, OTHER_LOCATORS


@when("we click on {tab_label} tab")
def click_on_tab(context, tab_label: str):
    tab_selector = get_element(
        context,
        NAVIGATION_BAR_LOCATORS[tab_label]["type"],
        NAVIGATION_BAR_LOCATORS[tab_label]["locator"],
    )
    tab_selector.click()


@when("we add random item to the cart")
def add_random_item_to_the_cart(context):
    while True:
        random_item = random.randint(
            1,
            len(get_elements(context, "xpath", "//ul[@class='products columns-4']/li")),
        )
        context.item_name = get_element(
            context, "xpath", f"//ul[@class='products columns-4']/li[{random_item}]"
        ).text
        try:
            element = get_element(
                context,
                "xpath",
                f"//ul[@class ='products columns-4']/li[{random_item}]/a[text()='Add to cart']",
            )
            context.elements_id = element.get_attribute("data-product_id")
            element.click()
            break
        except NoSuchElementException:
            pass


@then("the page title is {text}")
def page_title(context, text: str):
    assert text == f"{context.driver.title}"


@then("the randomly selected item is in the cart")
def is_randomly_selected_item_in_the_cart(context):
    assert_element_is_present(
        context,
        "xpath",
        f".//ul[contains(@class,'woocommerce-mini-cart')]//a[@data-product_id='{context.elements_id}']",
    )


@then("the {tab_label} tab is present")
def tab_is_present(context, tab_label):
    tab = get_element(
        context, "xpath", f".//ul[@class='nav-menu']//a[text()='{tab_label}']"
    )
    assert_element_is_visible(tab)


@then("there are {items_in_cart} items in the cart")
def number_of_items_in_the_cart(context, items_in_cart: str):
    items_in_cart_label = get_element(context, "css", "a.cart-contents span.count").text
    number_of_items = items_in_cart_label.split()[0]
    assert items_in_cart == number_of_items


@then("there is 1 item in the cart")
def one_item_in_the_cart(context):
    items_in_cart_label = get_element(
        context,
        OTHER_LOCATORS["number_of_items_in_cart"]["type"],
        OTHER_LOCATORS["number_of_items_in_cart"]["locator"],
    ).text
    number_of_items = items_in_cart_label.split()[0]
    assert_text_equal(number_of_items, "1")

from behave import given
from selenium import webdriver


@given("we are present on the {text} page")
def go_to_page(context, text: str = None):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    pages = {
        "home": "http://demostore.supersqa.com",
        "cart": "http://demostore.supersqa.com/cart/",
        "checkout": "http://demostore.supersqa.com/checkout/",
        "my account": "http://demostore.supersqa.com/my-account/",
        "sample": "http://demostore.supersqa.com/sample-page/",
    }
    context.driver.get(pages[text]) if text in pages.keys() else context.driver.get(
        "http://demostore.supersqa.com"
    )

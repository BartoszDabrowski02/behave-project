from behave import given


@given("we are present on the {text} page")
def go_to_page(context, text: str = None):
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

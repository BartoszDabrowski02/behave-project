from behave import then

from base.assertions import assert_element_is_visible
from base.functions import get_element
from locators.demostore_locators import MY_ACCOUNT_PAGE_LOCATORS


@then("the {input_name} is present")
def input_is_visible(context, input_name):
    input = get_element(
        context,
        MY_ACCOUNT_PAGE_LOCATORS[input_name]["type"],
        MY_ACCOUNT_PAGE_LOCATORS[input_name]["locator"],
    )
    assert_element_is_visible(input)

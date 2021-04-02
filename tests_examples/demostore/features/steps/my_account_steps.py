from behave import then, when

from base.assertions import assert_element_is_visible, assert_text_equal
from base.functions import get_element, send_keys_with_delay
from locators.demostore_locators import MY_ACCOUNT_PAGE_LOCATORS


@when("we fill the password for a new account field with {text} value")
def fill_new_account_password_input(context, text):
    input = get_element(
        context,
        MY_ACCOUNT_PAGE_LOCATORS["new_account_password_input"]["type"],
        MY_ACCOUNT_PAGE_LOCATORS["new_account_password_input"]["locator"],
    )
    send_keys_with_delay(input, text, delay=0.25)


@then("the statement that your password is very weak appears")
def very_weak_password_statement(context):
    statement_text = get_element(
        context,
        MY_ACCOUNT_PAGE_LOCATORS["new_account_password_statement"]["type"],
        MY_ACCOUNT_PAGE_LOCATORS["new_account_password_statement"]["locator"],
    ).text
    assert_text_equal(statement_text, "Very weak - Please enter a stronger password.")


@then("the {input_name} is present")
def input_is_visible(context, input_name):
    input = get_element(
        context,
        MY_ACCOUNT_PAGE_LOCATORS[input_name]["type"],
        MY_ACCOUNT_PAGE_LOCATORS[input_name]["locator"],
    )
    assert_element_is_visible(input)

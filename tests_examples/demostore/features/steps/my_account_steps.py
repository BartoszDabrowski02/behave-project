from behave import then

from base.assertions import assert_element_is_visible
from base.functions import get_element


@then("the {input_name} input is present")
def input_is_visible(context, input_name):
    input = get_element(context, "css", f"input[name='{input_name}']")
    assert_element_is_visible(input)

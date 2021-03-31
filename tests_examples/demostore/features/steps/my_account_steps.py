from behave import then


@then("the {input_name} input is present")
def input_is_visible(context, input_name):
    context.driver.find_element_by_css_selector(f"input[name='{input_name}']").is_displayed()

from base.functions import get_element


DEFAULT_ASSERTION_MESSAGES = {
    "assert_element_is_visible": "We expect that element is visible.",
    "assert_element_is_present": "We expect that element is present.",
}


def _default_assertion_message(method_name):
    return DEFAULT_ASSERTION_MESSAGES[method_name]


def assertion_message(assertion_name, *args, msg=None):
    if msg == None:
        msg = _default_assertion_message(assertion_name).format(*args)
    raise Exception(msg)


def assert_element_is_present(context, locator_type, locator, msg=None):
    if not get_element(context, locator_type, locator):
        assertion_message("assert_element_is_present", msg=msg)


def assert_element_is_visible(element, msg=None):
    if not element.is_displayed():
        assertion_message("assert_element_is_visible", msg=msg)

from behave import *

@given('test 123')
def generate_order_number(context):
    context.x = '123456'
    print(context.order_number)

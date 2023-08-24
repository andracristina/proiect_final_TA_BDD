from pages.checkout2_page import CheckoutPage2
from behave import *

check_out_page2 = CheckoutPage2()


@then('check_out_page2: I should land on the second checkout page')
def step_impl(context):
    check_out_page2.validate_correct_checkout2_url()


@when('check_out_page2: I click the finish button')
def step_impl(context):
    check_out_page2.click_finish_button()

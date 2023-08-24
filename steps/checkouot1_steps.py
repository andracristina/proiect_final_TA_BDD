from behave import *
from pages.checkout1_page import CheckoutPage1

check_out_page1 = CheckoutPage1()

@then ('check_out_page1: I should land on the first checkout page')
def step_impl(context):
    check_out_page1.validate_correct_checkout1_url()

@when ('check_out_page1: I enter my first name')
def step_impl(context):
    check_out_page1.enter_first_name()

@when ('check_out_page1: I enter my last name')
def step_impl(context):
    check_out_page1.enter_last_name()

@when ('check_out_page1: I enter my postcode')
def step_impl(context):
    check_out_page1.enter_postcode()

@when ('check_out_page1: I click Continue')
def step_impl(context):
    check_out_page1.click_continue()



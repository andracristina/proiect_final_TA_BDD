from pages.home_page import HomePage
from behave import *

from pages.shopping_cart_page import ShoppingCartPage

shopping_cart_page = ShoppingCartPage()

@then ('shopping_cart_page: I can view the backpack in the shopping cart')
def step_impl(context):
    shopping_cart_page.validate_backpack_entry()

@when('shopping_cart_page: I click the checkout button')
def step_impl(context):
    shopping_cart_page.click_ckeckout_button()


@when('shopping_cart_page: I click the remove button')
def step_impl(context):
    shopping_cart_page.click_remove_button()


@then ('shopping_cart_page: I validate the backpack has been removed')
def step_impl(context):
    shopping_cart_page.validate_backpack_removal()






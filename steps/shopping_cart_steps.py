from pages.home_page import HomePage
from behave import *

from pages.shopping_cart_page import ShoppingCartPage

shopping_cart_page = ShoppingCartPage()

@then ('shopping_cart_page: I can view the backpack in the shopping cart')
def step_impl(context):
    shopping_cart_page.validate_backpack_entry()



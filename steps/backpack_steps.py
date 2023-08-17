from pages.home_page import HomePage
from behave import *

from pages.backpack_page import BackpackPage

backpack_page = BackpackPage()

@then('backpack_product_page: I should see the backpack product description page')
def step_impl(context):
    backpack_page.validate_correct_url()

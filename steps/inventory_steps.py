from pages.home_page import HomePage
from behave import *

from pages.inventory_page import InventoryPage

inventory_page = InventoryPage()


@then('inventory: I should land on the inventory page')
def step_impl(context):
    inventory_page.validate_correct_url()

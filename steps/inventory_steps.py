from time import sleep

from pages.home_page import HomePage
from behave import *

from pages.inventory_page import InventoryPage

inventory_page = InventoryPage()


@then('inventory: I should land on the inventory page')
def step_impl(context):
    inventory_page.validate_correct_url()


'''
Given I am a user on the Inventory page
When I select the backpack card
Then I should see the backpack product description page
'''
@given('inventory: I am on the inventory page')
def step_impl(context):
   inventory_page.validate_correct_url()

@when ('inventory:I select the backpack card')
def step_impl(context):
    inventory_page.add_backpack_item()


'''
Given I am on the inventory page
When I  click the backpack add to cart button
When I open the shopping cart
Then I can view the backpack in the shopping cart

'''
@when ('inventory: I  click the backpack add to cart button')
def step_impl(context):
    inventory_page.add_backpack_item()

@when ('inventory: I open the shopping cart')
def step_impl(context):
    inventory_page.click_shopping_cart_button()


@when ('inventory: I click the sorting drop-down menu')
def step_impl(context):
    inventory_page.open_sorting_options()

@when ('inventory: I select Name (Z to A) option')
def step_impl(context):
    inventory_page.select_ztoa_sorting()



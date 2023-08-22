from time import sleep
from behave import *
from pages.inventory_page import InventoryPage

inventory_page = InventoryPage()


@then('inventory: I should land on the inventory page')
def step_impl(context):
    inventory_page.validate_correct_url()

@given('inventory: I am on the inventory page')
def step_impl(context):
   inventory_page.validate_correct_url()

@when ('inventory:I select the backpack card')
def step_impl(context):
    inventory_page.add_backpack_item()


@when ('inventory: I  click the backpack add to cart button')
def step_impl(context):
    inventory_page.add_backpack_item()

@when ('inventory: I open the shopping cart')
def step_impl(context):
    inventory_page.click_shopping_cart_button()


@then ('inventory: I validate that 6 products are displayed')
def step_impl(context):
    inventory_page.validate_product_count(6)


@when ('inventory: I click the sorting drop-down menu')
def step_impl(context):
    inventory_page.open_sorting_options()

@when ('inventory: I select Name (Z to A) option')
def step_impl(context):
    inventory_page.select_ztoa_sorting()

@then ('inventory: I validate that the products are arranged in reverse alphabetical order')
def step_impl(context):
    inventory_page.validate_ztoa_sorting()

@when ('inventory: I click the menu button')
def step_impl(context):
    inventory_page.clik_menu_button()

@when ('inventory: I click the logout button')
def step_impl(context):
    inventory_page.clik_menu_button()


from pages.home_page import HomePage
from behave import *

'''
Given I am a user on the Home page
When I enter my username
And I enter my password
And I click the login button 
Then I should land on the Inventory page
'''

home_page = HomePage()

@given('home: I am a user on the Home page')
def step_impl(context):
    home_page.navigate_to_home_page()

@when('home: I enter my username')
def step_impl(context):
    home_page.fill_username_input()

@when('home: I enter my password')
def step_impl(context):
    home_page.fill_password_input()

@when('home: I click the login button')
def step_impl(context):
    home_page.click_login_button()


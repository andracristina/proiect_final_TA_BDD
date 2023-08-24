import time

from pages.home_page import HomePage
from behave import *

home_page = HomePage()


@given('home: I am a user on the Home page')
def step_impl(context):
    home_page.driver.delete_all_cookies()
    home_page.navigate_to_home_page()


@when('home: I login with user {user} and password {password}')
def step_impl(context, user, password):
    home_page.fill_username_input(user)
    home_page.fill_password_input(password)
    home_page.click_login_button()
    time.sleep(2)


@then('home: I validate the correct invalid credentials error message is displayed')
def step_impl(context):
    home_page.validate_wrong_credentials_error()

@then('home: I validate the correct locked out credentials error message is displayed')
def step_impl(context):
    home_page.validate_locked_credentials_error()

@then('home: I should land on the home page')
def step_impl(context):
    home_page.validate_correct_url()

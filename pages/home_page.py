from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # definim selectors

    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//*[@id="login-button"]'

 # actions
    def navigate_to_home_page(self):
        self.driver.get('https://www.saucedemo.com/')

    def fill_username_input(self):
        self.wait_for_elem(self.USERNAME_INPUT)
        self.driver.find_element(By.XPATH, self.USERNAME_INPUT).send_keys('standard_user')

    def fill_password_input(self):
        self.wait_for_elem(self.PASSWORD_INPUT)
        self.driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys('secret_sauce')

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()




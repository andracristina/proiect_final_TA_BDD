from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # definim selectors

    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//*[@id="login-button"]'
    INVALID_CREDENTIALS_ERROR = '//*[@id="login_button_container"]/div/form/div[3]'

 # actions

    def navigate_to_home_page(self):
        self.driver.delete_all_cookies()
        self.driver.get('https://www.saucedemo.com/')

    def fill_username_input(self,user):
        self.wait_for_elem(self.USERNAME_INPUT)
        self.driver.find_element(By.XPATH, self.USERNAME_INPUT).send_keys(user)

    def fill_password_input(self,password):
        self.wait_for_elem(self.PASSWORD_INPUT)
        self.driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def validate_wrong_credentials_error(self):
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Epic sadface: Username and password do not match any user in this service'
        actual = self.driver.find_element(By.XPATH,self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, 'Error message is correct')

    def validate_locked_credentials_error(self):
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Epic sadface: Sorry, this user has been locked out.'
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, 'Error message is correct')

    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')





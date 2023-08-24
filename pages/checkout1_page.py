from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class CheckoutPage1(BasePage):

    FIRST_NAME_INPUT = '//input[@id="first-name"]'
    LAST_NAME_INPUT = '//input[@id="last-name"]'
    POSTCODE_INPUT = '//input[@id="postal-code"]'
    CONTINUE_BUTTON = '//*[@id="continue"]'

    def validate_correct_checkout1_url(self):
        expected = 'https://www.saucedemo.com/checkout-step-one.html'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')

    def enter_first_name(self):
        self.wait_for_elem(self.FIRST_NAME_INPUT)
        self.driver.find_element(By.XPATH, self.FIRST_NAME_INPUT).send_keys('Andra')

    def enter_last_name(self):
        self.wait_for_elem(self.LAST_NAME_INPUT)
        self.driver.find_element(By.XPATH, self.LAST_NAME_INPUT).send_keys('Trifu')

    def enter_postcode(self):
        self.wait_for_elem(self.POSTCODE_INPUT)
        self.driver.find_element(By.XPATH, self.POSTCODE_INPUT).send_keys('L91AF')

    def click_continue(self):
        self.wait_for_elem(self.CONTINUE_BUTTON)
        self.driver.find_element(By.XPATH, self.CONTINUE_BUTTON).click()
        sleep(1)

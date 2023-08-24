from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage2(BasePage):

    FINISH_BUTTON = '//button[@id="finish"]'

    def validate_correct_checkout2_url(self):
        expected = 'https://www.saucedemo.com/checkout-step-two.html'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')

    def click_finish_button(self):
        self.wait_for_elem(self.FINISH_BUTTON)
        self.driver.find_element(By.XPATH,self.FINISH_BUTTON).click()

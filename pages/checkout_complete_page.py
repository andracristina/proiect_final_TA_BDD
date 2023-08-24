from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    BACK_HOME_BUTTON = '//button[@id="back-to-products"]'

    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/checkout-complete.html'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')

    def click_back_home_button(self):
        self.wait_for_elem(self.BACK_HOME_BUTTON)
        self.driver.find_element(By.XPATH, self.BACK_HOME_BUTTON).click()

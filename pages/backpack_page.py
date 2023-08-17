from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BackpackPage(BasePage):
    ADD_TO_CART_BUTTON = '//button[@id="add-to-cart-sauce-labs-backpack"]'

    def click_add_to_card(self):
        self.wait_for_elem(self.ADD_TO_CART_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON).click()

    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/inventory-item.html?id=4'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')
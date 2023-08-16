from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    BACKPACK = '//div[text()="Sauce Labs Backpack"]'

    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/inventory.html'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):

    CART_ENTRY_BACKPACK = '//*[@id="item_4_title_link"]/div'
    CHECKOUT_BUTTON = '//*[@id="checkout"]'
    REMOVE_BUTTON = '//*[@id="remove-sauce-labs-backpack"]'

    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/cart.html'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')

    def validate_backpack_entry(self):
        self.wait_for_elem(self.CART_ENTRY_BACKPACK)
        if self.driver.find_element(By.XPATH,self.CART_ENTRY_BACKPACK).is_displayed():
            print("The product has been added")
        else:
            print("Error, product not in cart")

    def validate_backpack_removal(self):
        try:
            element = self.driver.find_element(By.XPATH, self.CART_ENTRY_BACKPACK)
            return not element.is_displayed()
        except:
            return True

    def click_ckeckout_button(self):
        self.wait_for_elem(self.CHECKOUT_BUTTON)
        self.driver.find_element(By.XPATH, self.CHECKOUT_BUTTON).click()

    def click_remove_button(self):
        self.wait_for_elem(self.REMOVE_BUTTON)
        self.driver.find_element(By.XPATH,self.REMOVE_BUTTON).click()


    def browser_back(self):
        self.driver.back()



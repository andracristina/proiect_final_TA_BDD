from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):

    CART_ENTRY_BACKPACK = '//*[@id="item_4_title_link"]/div'

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



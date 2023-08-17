import products as products
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    BACKPACK = '//div[text()="Sauce Labs Backpack"]'
    ADD_TO_CART_BACKPACK_BUTTON = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    SHOPPING_CART_BUTTON = '//*[@id="shopping_cart_container"]/a'
    SORTING_MENU = '//*[@id="header_container"]/div[2]/div/span/select'
    PRODUCT_CARD_ELEMENTS = '//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]'
    PRODUCT_NAME = '//*[@id="item_3_title_link"]/div'
    products = []

    ZtoA = '//*[@id="header_container"]/div[2]/div/span/select/option[2]'



    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/inventory.html'
        actual = self.driver.current_url
        self.assertEqual(expected,actual,'URL is incorrect')

    def navigate_to_inventory_page(self):
        self.driver.get('https://www.saucedemo.com/inventory.html')

    def add_backpack_item(self):
        self.wait_for_elem(self.ADD_TO_CART_BACKPACK_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_TO_CART_BACKPACK_BUTTON).click()

    def click_add_backpack_to_cart_button(self):
        self.wait_for_elem(self.ADD_TO_CART_BACKPACK_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_TO_CART_BACKPACK_BUTTON).click()

    def click_shopping_cart_button(self):
        self.wait_for_elem(self.SHOPPING_CART_BUTTON)
        self.driver.find_element(By.XPATH, self.SHOPPING_CART_BUTTON).click()

    def open_sorting_options(self):
        self.wait_for_elem(self.SORTING_MENU)
        self.driver.find_element(By.XPATH, self.SORTING_MENU).click()

    def select_ztoa_sorting(self):
        self.wait_for_elem(self.ZtoA)
        self.driver.find_element(By.XPATH, self.ZtoA).click()






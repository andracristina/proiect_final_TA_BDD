from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class InventoryPage(BasePage):
    BACKPACK = '//div[text()="Sauce Labs Backpack"]'
    ADD_TO_CART_BACKPACK_BUTTON = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    SHOPPING_CART_BUTTON = '//*[@id="shopping_cart_container"]/a'
    SORTING_MENU = '//*[@id="header_container"]/div[2]/div/span/select'
    AVAILABLE_ITEMS = '//*[@class="inventory_item"]'
    PRODUCTS_AVAILABLE = ['//*[@class="inventory_item"]']
    ZtoA = '//*[@id="header_container"]/div[2]/div/span/select/option[2]'
    MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    LOGOUT_BUTTON = '//a[text()="Logout"]'

    def validate_correct_url(self):
        expected = 'https://www.saucedemo.com/inventory.html'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'URL is incorrect')

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

    def validate_product_count(self, expected_number):
        sleep(1)
        actual_number = len(self.driver.find_elements(By.XPATH, self.AVAILABLE_ITEMS))
        self.assertEqual(expected_number, actual_number, 'Number of products is incorrect')

    def open_sorting_options(self):
        self.wait_for_elem(self.SORTING_MENU)
        self.driver.find_element(By.XPATH, self.SORTING_MENU).click()

    def select_ztoa_sorting(self):
        self.wait_for_elem(self.ZtoA)
        self.driver.find_element(By.XPATH, self.ZtoA).click()

    def validate_ztoa_sorting(self):
        sorted_products = sorted(self.PRODUCTS_AVAILABLE, reverse=True)
        assert self.PRODUCTS_AVAILABLE == sorted_products, "Products are not sorted correctly"

    def clik_menu_button(self):
        self.wait_for_elem(self.MENU_BUTTON)
        self.driver.find_element(By.XPATH, self.MENU_BUTTON).click()

    def clik_logout_button(self):
        self.wait_for_elem(self.LOGOUT_BUTTON)
        element = self.driver.find_element(By.XPATH, self.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

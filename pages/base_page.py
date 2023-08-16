from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, selector):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, selector)))

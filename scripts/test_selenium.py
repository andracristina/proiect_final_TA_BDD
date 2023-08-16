from time import sleep

from selenium import webdriver
chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://the-internet.herokuapp.com/login')

sleep(3)

chrome.quit()

print('SUCCESS - TEST PASSED')
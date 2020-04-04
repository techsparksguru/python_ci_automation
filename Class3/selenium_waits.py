from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import selenium exceptions module
from selenium.common.exceptions import * 

browser = webdriver.Chrome()
browser.get("http://www.seleniumframework.com/python-course/")
browser.maximize_window()

browser.implicitly_wait(10)

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "randomtag"))
    )
except TimeoutException:
    print("Encounted timeout while waiting for the element")
else:
    print("Successfully located all the elements by tag name")

browser.quit()
import time 

# Import webdriver module from selenium
from selenium import webdriver

# import selenium exceptions module
from selenium.common.exceptions import * 

# Create a webdriver instance for chrome browser
browser = webdriver.Chrome()

# GoTo (Go to a URL)
browser.get("http://www.seleniumframework.com/python-course/")
browser.maximize_window()

# Refresh page
browser.refresh()

# Wait for the elements to load
browser.implicitly_wait(30)


try:
    # Locate element using XPATH
    name = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div/span[1]/input')
    name.send_keys("FirstName")

    # Locate element by ID
    email = browser.find_element_by_id("form-validation-field-17474")
    email.send_keys("abc@xyz.com")

except NoSuchElementException as error:
    print("Could not find the element due to the error, {}".format(error))
    email = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div/span[1]/input')
    email.send_keys("abc@xyz.com")


try:
    email = browser.find_element_by_class_name("form-mail")
    email.send_keys("abc@xyz.com")

except ElementNotInteractableException as error:
    print("Could not interact with the element due to the error, {}".format(error))
    email = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div/span[1]/input')
    email.clear()
    email.send_keys("suhas123@xyz.com")

try: 
    frame = browser.switch_to.frame("SeleniumHandle")

except NoSuchFrameException as error:
    print("Couldn't switch to the frame. Encountered with {} exception".format(error))

try: 
    frame = browser.switch_to.window("1372823843")

except NoSuchWindowException as error:
    print("Couldn't switch to the window. Encountered with {} exception".format(error))

finally:
    browser.quit()
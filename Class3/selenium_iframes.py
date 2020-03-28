import time

# Import webdriver module from selenium
from selenium import webdriver

# import selenium exceptions module
from selenium.common.exceptions import * 

# Create a webdriver instance for chrome browser
browser = webdriver.Chrome()

browser.get('file:///home/suhas/techsparks/python_ci_automation/Class3/iframe.html')                                                                                                                                              
browser.maximize_window()

try:
    browser.find_element_by_link_text('HERE').click()

except Exception as error:
    print(error + '\n')

# Switch to the second IFrame
browser.switch_to.frame('frame2')

browser.find_element_by_link_text('HERE').click()

time.sleep(8)

browser.quit()
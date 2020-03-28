import time 

# Import webdriver module from selenium
from selenium import webdriver

# import selenium exceptions module
from selenium.common.exceptions import *

# import keys module
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.seleniumframework.com/python-course/")
browser.implicitly_wait(30)
browser.maximize_window()

actionchains = webdriver.ActionChains(browser)

tutorials = browser.find_element_by_xpath('//*[@id="main-nav"]/li[2]/a')
hover_tutorials = actionchains.click(tutorials)
hover_tutorials.perform()
time.sleep(12)

python = browser.find_element_by_xpath('//*[@id="main-nav"]/li[2]/ul/li[4]/a') 
hover_python = actionchains.click(python)   
hover_python.perform()

actionchains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()  

# click from the dynamic list
browser.find_element_by_xpath('//*[@id="main-nav"]/li[2]/ul/li[4]/ul/li/a/span').click()

browser.quit()
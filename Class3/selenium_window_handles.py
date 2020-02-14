import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.seleniumframework.com/python-course/")
browser.implicitly_wait(10)
browser.maximize_window()

# click the subscribe button
subscribe = browser.find_element_by_xpath('//*[@id="text-11"]/div/form/input[3]').click()


# Get the window handles and switch to the launched window
window_handles = browser.window_handles
browser.switch_to.window(window_handles[1])

browser.maximize_window()
time.sleep(5)

# Switch to new window and maximize
email_address = browser.find_element_by_xpath('//*[@id="pageHolder"]/div[1]/form/input[1]')                                                                                                                                          
email_address.send_keys('hello.world@email.com')

subscription_request = browser.find_element_by_xpath('//*[@id="pageHolder"]/div[1]/form/p[2]/input')                                                                                                                                 
subscription_request.click() 

browser.close()
time.sleep(3)
browser.quit()

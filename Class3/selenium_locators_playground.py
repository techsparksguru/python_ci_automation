#Import webdriver module from selenium
from selenium import webdriver

# Create a webdriver instance for chrome browser
browser = webdriver.Chrome()

# GoTo (Go to a URL)
browser.get("http://www.seleniumframework.com/python-course/")

# Locate element using XPATH
name = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div/span[1]/input')

# Locate element using ID and store it in a variable
email = browser.find_element_by_id("form-validation-field-1")

# Locate element by NAME
telephone = browser.find_element_by_name("telephone")

# Locate element by CLASS_NAME
country = browser.find_element_by_class_name("form-country")

# Locate element by TAG_NAME
image = browser.find_element_by_tag_name("img")

# Locate element by LINK_TEXT
browser.find_element_by_link_text("clear")

# Locate element by PARTIAL_LINK_TEXT
browser.find_element_by_partial_link_text("Sub")

# Locate multiple elements using find_by_elements method
images = browser.find_elements_by_tag_name("img")

# Locate element by CSS Selector
css_selector = browser.find_element_by_css_selector("#recent-posts-3 > ul > li:nth-child(1) > a")

# Play around with the located elements

# Fill the First Name Text Box by sending some value
name.send_keys("YourFirstName")

# Clear the FirstName text Field using clear() function
name.clear()

# Check if the selected element is a required field using its attributes/properties and assert statement
assert name.get_attribute('aria-required') == 'true'

# Check the errors by leaving the required fields blank and hitting Submit button in the form
browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/p/a[1]').click()

error_log = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/aside/div/section[2]/form/div/span[1]/div/div[1]').text
assert error_log == "* This field is required"
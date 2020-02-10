import time 

#Import webdriver module from selenium
from selenium import webdriver

# Create a webdriver instance for chrome browser
browser = webdriver.Chrome()

# GoTo (Go to a URL)
browser.get("http://www.seleniumframework.com/python-course/")
browser.maximize_window()

# Refresh page
browser.refresh()

# Wait for the elements to load
browser.implicitly_wait(30)

# Find the form-fields
form_area = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div')
form_fields = form_area.find_elements_by_tag_name('input')

# Iterate through the fields and fill the 
for field in form_fields:
    print("Filling the field {}".format(field.get_attribute('name')))
    if field.get_attribute('name') == 'telephone':
        field.send_keys('12883474738')
    elif field.get_attribute('name') == 'email':
            field.send_keys('abc@xyz.com')
    else:
        field.send_keys('TestField')


# Message Field
message = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/span/textarea')
message.send_keys('Welcome to the SeleniumFramework Automation Course')

# Submit Button
submit_form = browser.find_element_by_partial_link_text("Sub")
submit_form.click()


















# name = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div/span[1]/input')
# name.send_keys("FirstName")

# email = browser.find_element_by_class_name("form-mail")
# touchactions.tap(email)
# email.send_keys("abc@xyz.com")

# telephone = browser.find_element_by_name("telephone")
# telephone.send_keys("12348937")


# # Message text area
# message = browser.find_element_by_class_name("form-message")
# message.send_keys("Filling in the course registration form")

# # Click the submit button
# browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/p/a[1]').click()
browser.quit()

# try:
#     # Locate element using XPATH
#     name = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div/span[1]/input')
#     name.send_keys("FirstName")

#     # Locate element using ID and store it in a variable
#     email = browser.find_element_by_id("form-validation-field-1")
#     email.send_keys("abc@xyz.com")

#     # Locate element by NAME
#     telephone = browser.find_element_by_name("telephone")
#     telephone.send_keys("12348937")

#     # Message text area
#     message = browser.find_element_by_class_name("form-message")
#     message.send_keys("Filling in the test registration form")

#     # Click the submit button
#     browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/p/a[1]').click()

# except Exception:
#     print("Could not find the element")

# finally:
    # browser.quit()
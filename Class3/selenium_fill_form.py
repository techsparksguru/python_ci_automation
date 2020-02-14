import time 

# Import webdriver module from selenium
from selenium import webdriver

# Create a webdriver instance for chrome browser
browser = webdriver.Chrome()

# GoTo (Go to a URL)
browser.get("http://www.seleniumframework.com/python-course/")
browser.maximize_window()

# Refresh page
browser.refresh()

# Wait for the elements to load
browser.implicitly_wait(20)

# Find the form-fields
form_area = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form')
form_fields = form_area.find_elements_by_tag_name('input')
form_fields = form_fields[2:-1]
form_fields.append(form_area.find_element_by_tag_name('textarea'))

# Iterate through the fields and fill the 
for field in form_fields:
    if field.get_attribute('aria-required')=='true'):
        print("Filling the required field {}".format(field.get_attribute('name')))
    else:
        print("Filling the field {}".format(field.get_attribute('name')))

    if field.get_attribute('name') == 'telephone':
        field.send_keys('12883474738')
    elif field.get_attribute('name') == 'email':
        field.send_keys('abc@xyz.com')
    elif field.get_attribute('name') == 'message':
        field.send_keys('SeleniumFramework Automation Course Registration')
    else:
        field.send_keys('TestField')

    time.sleep(3)

# Submit Button
submit_form = form_area.find_element_by_partial_link_text("Sub")
print('Clicking the Submit button')
submit_form.click()

browser.implicitly_wait(30)

toast_message = browser.find_element_by_xpath('//*[@id="presscore-contact-form-widget-3"]/form/div[1]/div')
assert toast_message.text == 'Feedback has been sent to the administrator'
time.sleep(10)

# Quits the webdriver session
browser.quit()
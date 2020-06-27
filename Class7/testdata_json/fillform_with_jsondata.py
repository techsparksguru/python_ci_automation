import json,time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

practice_dict = json.loads(open("practiceform.json").read())

browser = webdriver.Chrome()
browser.get('http://www.practiceselenium.com/practice-form.html')

print(practice_dict)
for row in practice_dict["table"]:
    current_row = row
    browser.find_element_by_name("firstname").send_keys(current_row['firstname'])
    browser.find_element_by_name("lastname").send_keys(current_row['lastname'])
    browser.find_element_by_id('sex-1').click()
    browser.find_element_by_id('datepicker').send_keys(current_row["date_stopped"])
    browser.find_element_by_id('tea2').click()
    browser.find_element_by_id('tool-1').click()
    continents_select = Select(browser.find_element_by_id('continents'))
    continents_select.options[0].click()
    another_select_list = Select(browser.find_element_by_id('selenium_commands'))
    another_select_list.options[0].click()
    time.sleep(5)
    browser.refresh()

browser.quit()
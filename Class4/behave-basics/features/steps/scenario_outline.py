from behave import *
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import WebDriverException
import unittest
import time
 
import traceback 

use_step_matcher('re')

@when("I open practiceselenium website")
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com/practice-form.html")

	
@step('I fill "(?P<firstname>.+)" "(?P<lastname>.+)" "(?P<sex>.+)" "(?P<yrs>.+)" "(?P<date_stopped>.+)"')
def step_impl(context, firstname, lastname, sex, yrs, date_stopped):
    context.browser.find_element_by_name("firstname").send_keys(firstname)
    context.browser.find_element_by_name("lastname").send_keys(lastname)
    sex_element = next(element for element in context.browser.find_elements_by_name("sex"))
    sex_element.click()
    yrs_element = next(element for element in context.browser.find_elements_by_tag_name("input"))
    yrs_element.click()
    context.browser.find_element_by_id('datepicker').send_keys(date_stopped)

@when('I fill "(?P<tea>.+)" "(?P<excited_about>.+)" "(?P<continent>.+)" and "(?P<selenium_commands>.+)"')
def step_impl(context, tea, excited_about, continent, selenium_commands):
    tea_element = next(element for element in context.browser.find_elements_by_tag_name("input") if element.get_attribute("value")==tea)
    tea_element.click()
    excited_element = next(element for element in context.browser.find_elements_by_name("tool") if element.get_attribute("value")==excited_about)
    excited_element.click()
 
    continents_select = Select(context.browser.find_element_by_id('continents'))
    continents_element = next(element for element in continents_select.options if element.text==continent)
    continents_element.click()
 
    another_select_list = Select(context.browser.find_element_by_id('selenium_commands'))
    another_select_element = next(element for element in another_select_list.options if element.text==selenium_commands)
    another_select_element.click()
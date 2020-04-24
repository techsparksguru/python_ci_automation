from behave import *
from selenium.webdriver.support.ui import Select 
 
@step("I fill the form with values")
def step_impl(context):
    context.browser.find_element_by_name("firstname").send_keys("Pradeep")
    context.browser.find_element_by_name("lastname").send_keys("Kumar")
    context.browser.find_element_by_id('sex-1').click()
    context.browser.find_element_by_id('datepicker').send_keys("1/1/2012")
    context.browser.find_element_by_id('tea2').click()
    context.browser.find_element_by_id('tool-1').click()
    continents_select = Select(context.browser.find_element_by_id('continents'))
    continents_select.options[0].click()
    another_select_list = Select(context.browser.find_element_by_id('selenium_commands'))
    another_select_list.options[0].click()
 
@step("I hit submit button")
def step_impl(context):
    context.browser.find_element_by_id('submit').click()
 
@then("I go back to Welcome page and verify title")
def step_impl(context):
    title = context.browser.title
    assert 'Welcome' in title
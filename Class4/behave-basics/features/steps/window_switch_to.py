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
 
@when("I open seleniumframework website")
def step_impl(context):
    context.browser.get("http://www.seleniumframework.com/PracticeForm")
    
@step("I click open new browser window")
def step_impl(context):
    context.browser.find_element_by_id("button1").click()
 
 
@then("I switch to new window")
def step_impl(context):
    print("Parent Handle:"+context.browser.current_window_handle)
    print("Parent Window title:"+context.browser.title)
    print("Now printing all handles...")
    #http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
    for idx, handle in enumerate(context.browser.window_handles):
        print("Handle-"+str(idx)+"-"+handle)
    print("Switching to child window")
    context.browser.switch_to_window(context.browser.window_handles[1])
    print("Window title after switching to child window--"+context.browser.title)
 
@step("back to parent window")
def step_impl(context):
    print("Switching to parent window")
    context.browser.switch_to_window(context.browser.window_handles[0])
    print("Windows title after switching to parent window--"+context.browser.title)
 
 
@step("I click javascript alert window")
def step_impl(context):
    context.browser.find_element_by_id("alert").click()
    try:
        WebDriverWait(context.browser, 10).until(EC.alert_is_present())
    except(TimeoutException):
        traceback.print_exc()
 
@then("I print the text in javascript alert")
def step_impl(context):
    alert = context.browser.switch_to_alert()
    print(alert.text)
 
 
@step("I click new browser tab")
def step_impl(context):
    # The below returns a list, though we assume that there is only one exact match in the list
    #new_browser_tab = filter(lambda element: element.text=='New Browser Tab' ,context.browser.find_elements_by_tag_name("button"))
    # The second way to do is as below
    new_browser_tab = [element for element in context.browser.find_elements_by_tag_name("button") if element.text=="New Browser Tab"]
    new_browser_tab[0].click()
 
@then("I switch to new tab")
def step_impl(context):
    print("Parent Handle:"+context.browser.current_window_handle)
    print("Parent Window title:"+context.browser.title)
    print("Now printing all handles...")
    #http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
    for idx, handle in enumerate(context.browser.window_handles):
        print("Handle-"+str(idx)+"-"+handle)
 
    print("Switching to browser tab")
    context.browser.switch_to.window(context.browser.window_handles[1])
    print("Window title after switching to browser tab--"+context.browser.title)
 
 
@step("back to main window")
def step_impl(context):
    print("Switching to parent window")
    context.browser.switch_to.window(context.browser.window_handles[0])
    print("Windows title after switching to parent window--"+context.browser.title)
 
@step("I click new message window button")
def step_impl(context):
    # The below returns a list, though we assume that there is only one exact match in the list
    #new_browser_tab = filter(lambda element: element.text=='New Message Window' ,context.browser.find_elements_by_tag_name("button"))
    # The second way to do is as below
    new_message_window = [element for element in context.browser.find_elements_by_tag_name("button") if element.text=="New Message Window"]
    new_message_window[0].click()
 
@then("I print text for message window")
def step_impl(context):
    # Note that message window on chrome throws an error "Disable chrome extensions" - so execute on firefox and good
    print("Parent Handle:"+context.browser.current_window_handle)
    print("Parent Window title:"+context.browser.title)
    print("Now printing all handles...")
    #http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
    for idx, handle in enumerate(context.browser.window_handles):
        print("Handle-"+str(idx)+"-"+handle)
 
    print("Switching to message window")
    context.browser.switch_to.window(context.browser.window_handles[1]) 
 
@when("I open yourhtmlsource website")
def step_impl(context):
    context.browser.get("http://yourhtmlsource.com/frames/inlineframes.html")
 
 
@then("I switch to frame and print its text")
def step_impl(context):
    all_iframes = context.browser.find_elements_by_tag_name("iframe")
    bomb_iframe = next(iframe for iframe in all_iframes if iframe.get_attribute("name")=='bomb')
    print("Switching to iframe whose name is 'bomb'")
    context.browser.switch_to_frame(bomb_iframe)
    print("Printing the body html for the iframe")
    print(context.browser.find_element_by_tag_name("body").text)
    print("Switching back to parent frame...")
    context.browser.switch_to_default_content()
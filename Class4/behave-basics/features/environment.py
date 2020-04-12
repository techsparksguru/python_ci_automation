import os
import sys
#import zipfile
import shutil
import time
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()


def before_all(context):
    print("Executing before all")
    if os.path.exists("failed_scenarios_screenshots"):
        shutil.rmtree('failed_scenarios_screenshots')

def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    #  context.logger = logging.getLogger('seleniumframework_tests')
    #  hdlr = logging.FileHandler('./seleniumframework_tests.log')
    #  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #  hdlr.setFormatter(formatter)
    #  context.logger.addHandler(hdlr)
    #  context.logger.setLevel(logging.DEBUG)

# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    chrome_options = Options()

    print("User data:", context.config.userdata)

    # behave -D BROWSER=chrome
    if 'BROWSER' not in context.config.userdata.keys():
        BROWSER='chrome'

    elif 'BROWSER' in context.config.userdata.keys():
        BROWSER = context.config.userdata['BROWSER']

    # For some reason, python doesn't have switch case -
    # http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python


    if 'GRID' in context.config.userdata.keys():
        if context.config.userdata['GRID'] == 'yes':
            if 'URL' in context.config.userdata.keys():
                if context.config.userdata['URL'] is None:
                    print("GRID URL is invalid & Quiting the browser")
                    sys.exit()
                else:
                    URL = context.config.userdata['URL']

                if BROWSER == 'chrome':
                    context.browser = webdriver.Remote(command_executor=URL,
                                                       desired_capabilities={"browserName": "chrome"})
                elif BROWSER == 'firefox':
                    context.browser = webdriver.Remote(command_executor=URL,
                                                       desired_capabilities={"browserName": "firefox"})
                else:
                    print("Browser you entered:", BROWSER, "is invalid value")
    
    if BROWSER == 'chrome':
        if ('HEADLESS' in context.config.userdata.keys()) or ('headless.scenario' in scenario.tags):
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument('--no-sandbox')
            context.browser = webdriver.Chrome(chrome_options=chrome_options)
        else:
            context.browser = webdriver.Chrome()
            context.browser.maximize_window()
            
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
        context.browser.maximize_window()

    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
        context.browser.maximize_window()

    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
        context.browser.maximize_window()

    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
        context.browser.maximize_window()

    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
        
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

def after_scenario(context, scenario):
    print("scenario status " + str(scenario.status))
    if scenario.status == "Status.failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
        os.chdir("..")
    context.browser.quit()

def after_feature(context, feature):
    print("\nAfter Feature")

def after_all(context):
    print("Executing after all")
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            if context.config.userdata['ARCHIVE'] == "Yes":
                shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")

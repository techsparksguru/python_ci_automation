import os
import sys
import zipfile
import shutil
import time
import logging
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()


def before_all(context):
    print("Executing before all")
    context.username = os.getenv("EMAIL_ID", "suhas290@gmail.com")
    context.passwd = os.getenv("PASSWORD", "open4al")
    paths = [
        'seleniumframework_tests.log',
        'failed_scenarios_screenshots'
    ]

    for filepath in paths:
        if os.path.exists(filepath):
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)

    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('seleniumframework_tests')
    hdlr = logging.FileHandler('seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    # behave -D BROWSER=chrome
    context.logger.info("Running Shopping Cart UI Test: Scenario {}".format(scenario.name))

    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    # For some reason, python doesn't have switch case -
    # http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    if(('HEADLESS' in context.config.userdata.keys()) and BROWSER == 'chrome'):
        print(context.config.userdata['HEADLESS'])
        if (context.config.userdata['HEADLESS'].lower()) == 'true':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            context.browser = webdriver.Chrome(chrome_options=chrome_options)
        else:
            context.browser = webdriver.Chrome()

    elif BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print(("Browser you entered:", BROWSER, "is invalid value"))

    context.browser.maximize_window()
    print("Before scenario\n")


def after_scenario(context, scenario):
    print("scenario status " + str(scenario.status))
    if str(scenario.status) == "Status.failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(str(scenario.name) + "_failed.png")
        os.chdir("..")
        context.logger.error("The Scenario: {} failed due to TimeOut waiting for the element(s)".format(scenario.name))
    elif str(scenario.status) == "Status.passed":
        context.logger.info("The Scenario: {} passed without errors".format(scenario.name))

    context.browser.quit()

def after_feature(context, feature):
    print("\nAfter Feature")

def after_all(context):
    print("Executing after all")
    # behave -D ARCHIVE=Yes
    try:
        if 'ARCHIVE' in list(context.config.userdata.keys()):
            if context.config.userdata['ARCHIVE']:
                shutil.make_archive(time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
   
    except Exception as error:
        print(error)
        
    finally:
        context.logger.info("*************** End of Run ***************")
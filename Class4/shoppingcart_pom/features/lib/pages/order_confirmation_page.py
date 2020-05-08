__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage

class OrderConfirmationPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "page_heading":(By.CLASS_NAME,"page-heading"),
        "confirm_alert":(By.CLASS_NAME,"alert-success")
    }

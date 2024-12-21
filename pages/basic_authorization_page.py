import logging

import pyautogui
from scripts.regsetup import description
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.label import Label
from base.web_element import WebElement


class BasicAuthorizationPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")

    TEXT_CONGRATULATIONS = (By.XPATH, "//p[contains(text(),'Congratulations!')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'BasicAuthorization'
        self.unique_element = Label(self.browser, self.UNIQUE_LOC, description="Unique element page")
        self.text_congratulations = WebElement(self.browser, self.TEXT_CONGRATULATIONS,
                                               description="Login page ->text search ")

    def get_text_congratulations(self):
        return self.text_congratulations.get_text()

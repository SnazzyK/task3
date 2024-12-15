import logging

import pyautogui
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.class_web_element import WebElement


class BasicAuthorization(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")

    TEXT_CONGRATULATIONS = (By.XPATH, "//p[contains(text(),'Congratulations!')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'BasicAuthorization'

        self.text_congratulations = WebElement(self.browser, self.TEXT_CONGRATULATIONS,
                                               description="Login page ->text search ")

    def login(self, username, password):
        logging.info(f"{self.page_name}: login")
        pyautogui.typewrite(username)
        pyautogui.press("tab")
        pyautogui.typewrite(password)
        pyautogui.press("enter")

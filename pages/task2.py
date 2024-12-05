import logging

from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class JsAlert(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")

    BUTTON_JS_ALERT = (By.XPATH, "//*[@onclick='jsAlert()']")
    RESULT = (By.ID, "result")
    BUTTON_JS_CONFIRM = (By.XPATH, "//*[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//*[@onclick='jsPrompt()']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'JsAlert'

        self.button_click_alert = Button(self.driver, self.BUTTON_JS_ALERT,
                                         description="JsAlert page ->  JS Alert click")
        self.result = Label(self.driver, self.RESULT,
                            description="JsAlert page -> successfully result")
        self.button_click_confirm = Button(self.driver, self.BUTTON_JS_CONFIRM,
                                           description="JsAlert page ->  JS Confirm click")
        self.button_click_prompt = Button(self.driver, self.BUTTON_JS_PROMPT,
                                          description="JsAlert page ->  JS Prompt click")

    def click_button_alert(self):
        logging.info(f"{self.page_name}: alert")
        self.button_click_alert.click()

    def click_button_confirm(self):
        logging.info(f"{self.page_name}: confirm")
        self.button_click_confirm.click()

    def click_button_prompt(self):
        logging.info(f"{self.page_name}: prompt")
        self.button_click_prompt.click()

    def click_button_alert_js(self):
        logging.info(f"{self.page_name}: alert using JS")
        self.driver.execute_script("document.querySelector(\"[onclick='jsAlert()']\").click();")

    def click_button_confirm_js(self):
        logging.info(f"{self.page_name}: confirm using JS")
        self.driver.execute_script("document.querySelector(\"[onclick='jsConfirm()']\").click();")

    def click_button_prompt_js(self):
        logging.info(f"{self.page_name}: prompt using JS")
        self.driver.execute_script("document.querySelector(\"[onclick='jsPrompt()']\").click();")

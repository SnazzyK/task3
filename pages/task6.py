import logging
from operator import index
from tempfile import template

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.class_web_element import WebElement


class Hovers(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    HOVER_TEMPLATE = "//*[contains(@class ,'figure')][{index}]"
    TEXT_TEMPLATE = "//*[text()='name: user{index}']"

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'ContextClick'

    def get_hover_element(self, index):
        locator = (By.XPATH, self.HOVER_TEMPLATE.format(index=index))
        return WebElement(self.browser, locator, description=f"hover page -> hover {index} move")

    def get_text_element(self, index):
        locator = (By.XPATH, self.TEXT_TEMPLATE.format(index=index))
        return WebElement(self.browser, locator, description=f"hover page -> hover {index} check text")

    def check_hover(self, index):
        action = ActionChains(self.browser.driver)
        logging.info(f"{self.page_name}: move hover {index}")
        hover_element = self.get_hover_element(index).wait_for_visible()
        action.move_to_element(hover_element).perform()



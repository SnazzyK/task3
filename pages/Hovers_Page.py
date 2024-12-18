import logging
from operator import index
from tempfile import template

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.web_element import WebElement


class HoversPage(BasePage):
    # Локаторы с параметризацией типа и шаблона
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    HOVER_TEMPLATE = ("xpath", "//*[contains(@class ,'figure')][{index}]")
    TEXT_TEMPLATE = ("xpath", "//*[text()='name: user{index}']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "HoversPage"

    def build_locator(self, template, index):
        locator_type, locator_value = template
        formatted_value = locator_value.format(index=index)
        return getattr(By, locator_type.upper()), formatted_value

    def get_hover_element(self, index):
        locator = self.build_locator(self.HOVER_TEMPLATE, index)
        return WebElement(self.browser, locator, description=f"Hover page -> Hover {index} move")

    def get_text_element(self, index):
        locator = self.build_locator(self.TEXT_TEMPLATE, index)
        return WebElement(self.browser, locator, description=f"Hover page -> Hover {index} check text")

    def check_hover(self, index):
        action = ActionChains(self.browser.driver)
        logging.info(f"{self.page_name}: Move hover {index}")
        hover_element = self.get_hover_element(index).wait_for_visible()
        action.move_to_element(hover_element).perform()

    def check_text_of_hover(self, index):
        text_element = self.get_text_element(index)
        actual_text = text_element.get_text()
        expected_text = f"name: user{index}"
        logging.info(f"Expected text: {expected_text}, Actual text: {actual_text}")
        return actual_text == expected_text

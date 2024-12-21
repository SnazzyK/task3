import logging
from operator import index
from tempfile import template

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.web_element import WebElement


class HoversPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(text(),'Hovers')]")
    HOVER_TEMPLATE = (By.XPATH, "//*[contains(@class ,'figure')][{index}]")
    TEXT_TEMPLATE = (By.XPATH, "//*[text()='name: user{index}']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "HoversPage"
        self.unique_element = WebElement(self.browser, self.UNIQUE_LOC, description="unique element")
        self.hover_template = WebElement(self.browser, self.HOVER_TEMPLATE, description="hover template")
        self.text_template = WebElement(self.browser, self.TEXT_TEMPLATE, description="text template")

    def _get_element(self, locator_template, index_element):
        locator_type, locator_value = locator_template
        formatted_value = locator_value.format(index=index_element)
        locator = (locator_type, formatted_value)
        return WebElement(self.browser, locator,
                          description=f"Element with template {locator_template}, index {index_element}")

    def check_hover(self, index_element):
        logging.info(f"{self.page_name}: Move hover {index_element}")
        action = ActionChains(self.browser.driver)

        hover_element = self._get_element(self.HOVER_TEMPLATE, index_element).wait_for_visible()
        action.move_to_element(hover_element).perform()

    def check_text_of_hover(self, index_element):
        logging.info(f"{self.page_name}: Checking text of hover {index_element}")
        text_element = self._get_element(self.TEXT_TEMPLATE, index_element)
        actual_text = text_element.get_text()
        return actual_text

import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class Actions(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    SLIDER = (By.XPATH, "//input[contains(@onchange,'showValue')]")
    SLIDER_RESULT = (By.ID, "range")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'ContextClick'

        self.slider_move = WebElement(self.driver, self.SLIDER, description="Actions page ->  slider move")
        self.slider_result = WebElement(self.driver, self.SLIDER_RESULT, description="Actions page ->  slider result")

    def move_slider(self, value1, value2=0):
        action = ActionChains(self.driver)
        logging.info(f"{self.page_name}: box click")
        element = self.slider_move.wait_for_visible()
        action.drag_and_drop_by_offset(element, value1, value2).perform()

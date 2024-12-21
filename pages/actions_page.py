import logging
import random
import time
from enum import unique

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.label import Label
from base.web_element import WebElement
from utilities.logg_settings import Logger


class ActionsPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//h3[contains(text() , 'Horizontal Slider')]")
    SLIDER = (By.XPATH, "//input[contains(@onchange,'showValue')]")
    SLIDER_RESULT = (By.ID, "range")
    SLIDER_CONTAINS = (By.XPATH, "//*[contains(@class , 'sliderContainer')]")
    DEFAULT_STEP_SLIDER = (By.XPATH, "//input[@step]")
    STEP_BACK = 5

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'ContextClick'
        self.browser = browser
        self.slider_move = WebElement(self.browser, self.SLIDER, description="Actions page ->  slider move")
        self.slider_result = WebElement(self.browser, self.SLIDER_RESULT, description="Actions page ->  slider result")
        self.slider_contains = WebElement(self.browser, self.SLIDER_CONTAINS,
                                          description="Actions page ->  slider result")
        self.unique_element = Label(self.browser, self.UNIQUE_LOC, description="unique element page")
        self.default_step_slider = WebElement(self.browser, self.DEFAULT_STEP_SLIDER, description="default step slider")

    def random_move_slider(self, count, step_default):
        action = ActionChains(self.browser.driver)
        slider = self.slider_move.wait_for_visible()
        action.move_to_element(slider).click().perform()
        for i in range(self.STEP_BACK):
            action.key_down(Keys.ARROW_DOWN).perform()
            action.key_up(Keys.ARROW_DOWN).perform()

        action.send_keys(Keys.ARROW_DOWN).perform()
        logging.info(f"{self.page_name}: slider move")
        counter = 0
        for i in range(count):
            action.key_down(Keys.ARROW_UP).perform()
            action.key_up(Keys.ARROW_UP).perform()
            counter += float(step_default)
        return counter

    @staticmethod
    def get_format_number(number):
        rounded = round(number)
        return rounded if rounded == number else number

    def get_result_slider(self):
        return self.slider_result.get_text()

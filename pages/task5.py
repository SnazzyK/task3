import logging
import random
import time
from enum import unique

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.class_label import Label
from base.class_web_element import WebElement


class Actions(BasePage):
    UNIQUE_LOC = (By.XPATH, "//h3[contains(text() , 'Horizontal Slider')]")
    SLIDER = (By.XPATH, "//input[contains(@onchange,'showValue')]")
    SLIDER_RESULT = (By.ID, "range")
    SLIDER_CONTAINS = (By.XPATH,"//*[contains(@class , 'sliderContainer')]")


    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'ContextClick'
        self.browser = browser
        self.slider_move = WebElement(self.browser, self.SLIDER, description="Actions page ->  slider move")
        self.slider_result = WebElement(self.browser, self.SLIDER_RESULT, description="Actions page ->  slider result")
        self.slider_contains = WebElement(self.browser, self.SLIDER_CONTAINS, description="Actions page ->  slider result")
        self.unique_element = Label(self.browser,self.UNIQUE_LOC,description="unique element page")


    def random_move_slider(self, count):
        action = ActionChains(self.browser.driver)
        slider = self.slider_move.wait_for_visible()
        action.move_to_element(slider).click().perform()
        for i in range(5):
            action.key_down(Keys.ARROW_DOWN).perform()
            action.key_up(Keys.ARROW_DOWN).perform()
        time.sleep(0.5)
        action.send_keys(Keys.ARROW_DOWN).perform()
        logging.info(f"{self.page_name}: slider move")
        counter = 0
        for i in range(count):
            action.key_down(Keys.ARROW_UP).perform()
            action.key_up(Keys.ARROW_UP).perform()
            counter += 0.5
            time.sleep(0.5)
        return counter

    def format_number(self,number):
        if number % 1 == 0:
            return int(number)
        return number

    def unique_element_text(self):
        return self.unique_element.get_text()

    def slider_result(self):
        return self.slider_result.get_text()


import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class Hovers(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    HOVER_1 = (By.XPATH, "//*[@class ='figure'][1]")
    TEXT_1 = (By.XPATH, "//*[text()='name: user1']")

    HOVER_2 = (By.XPATH, "//*[@class ='figure'][2]")
    TEXT_2 = (By.XPATH, "//*[text()='name: user2']")

    HOVER_3 = (By.XPATH, "//*[@class ='figure'][3]")
    TEXT_3 = (By.XPATH, "//*[text()='name: user3']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'ContextClick'

        self.hover_1 = WebElement(self.driver, self.HOVER_1, description="hover page ->  hover 1 move")
        self.hover_2 = WebElement(self.driver, self.HOVER_2, description="hover page ->  hover 2 move")
        self.hover_3 = WebElement(self.driver, self.HOVER_3, description="hover page ->  hover 3 move")

        self.text_1 = WebElement(self.driver, self.TEXT_1, description="hover page ->  hover 1 check text")
        self.text_2 = WebElement(self.driver, self.TEXT_2, description="hover page ->  hover 2 check text")
        self.text_3 = WebElement(self.driver, self.TEXT_3, description="hover page ->  hover 3 check text")

    def check_hover_1(self):
        action = ActionChains(self.driver)
        logging.info(f"{self.page_name}: move hover 1")
        element_1 = self.hover_1.wait_for_visible()
        action.move_to_element(element_1).perform()

    def check_hover_2(self):
        action = ActionChains(self.driver)
        logging.info(f"{self.page_name}: move hover 2")
        element_2 = self.hover_2.wait_for_visible()
        action.move_to_element(element_2).perform()

    def check_hover_3(self):
        action = ActionChains(self.driver)
        logging.info(f"{self.page_name}: move hover 1")
        element_3 = self.hover_3.wait_for_visible()
        action.move_to_element(element_3).perform()

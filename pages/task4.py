import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class AlertsContextClick(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    BOX = (By.XPATH, "//*[@id='hot-spot']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'ContextClick'

        self.element_box_click = WebElement(self.driver, self.BOX, description="AlertsContextClick page ->  box click")

    def box_click(self):
        action = ActionChains(self.driver)
        logging.info(f"{self.page_name}: box click")
        element = self.element_box_click.wait_for_visible()
        action.move_to_element(element).context_click().perform()

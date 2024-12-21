import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.web_element import WebElement


class AlertsContextClickPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    BOX = (By.ID, "hot-spot")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'ContextClick'
        self.unique_element = WebElement(self.browser, self.UNIQUE_LOC, description="uniq element")
        self.element_box_click = WebElement(self.browser, self.BOX,
                                            description="Alerts Context Click page ->  box click right button")

    def wait_element_box_click(self):
        element = self.element_box_click.wait_for_visible()
        return element

    def click_box(self, element):
        logging.info(f"{self.page_name}: box click")
        self.element_box_click.move_and_context_click(element)

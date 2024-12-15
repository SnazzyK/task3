import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from base.base_page import BasePage
from base.class_web_element import WebElement


class AlertsContextClick(BasePage):
    UNIQUE_LOC = (By.XPATH, "//button[@type='submit']")
    BOX = (By.XPATH, "//*[@id='hot-spot']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'ContextClick'

        self.element_box_click = WebElement(self.browser, self.BOX, description="AlertsContextClick page ->  box click")

    def click_box(self):
        logging.info(f"{self.page_name}: box click")
        action = ActionChains(self.browser.driver)
        element = self.element_box_click.wait_for_visible()
        action.move_to_element(element).context_click().perform()

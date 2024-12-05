from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class Scroll(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[@class = 'example']")

    SCROLL_ADDED = (By.XPATH, "//div[@class = 'jscroll-added']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "scroll"

        self.scroll_added = WebElement(self.driver, self.SCROLL_ADDED,
                                       description="Scroll  page ->  added text")

    def found_elements(self):
        return self.scroll_added.wait_for_all_visible()

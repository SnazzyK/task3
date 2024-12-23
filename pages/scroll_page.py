from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.web_element import WebElement
from conftest import driver


class ScrollPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(@class , 'example')]")

    SCROLL_ADDED = (By.XPATH, "//div[@class = 'jscroll-added']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "scroll"

        self.unique_element = WebElement(self.browser, self.UNIQUE_LOC, description="unique element")

        self.scroll_added = WebElement(self.browser, self.SCROLL_ADDED,
                                       description="Scroll  page -> added text")

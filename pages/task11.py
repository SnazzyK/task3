from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.class_web_element import WebElement


class Scroll(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(@class , 'example')]")

    SCROLL_ADDED = (By.XPATH, "//div[@class = 'jscroll-added']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "scroll"

        self.scroll_added = WebElement(self.browser, self.SCROLL_ADDED,
                                       description="Scroll  page -> added text")

    def found_elements(self):
         return self.scroll_added.wait_for_all_visible()

    def scroll_body(self):
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

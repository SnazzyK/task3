from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.web_element import WebElement


class DynamicContentPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(@class , 'example')]")

    IMG = (By.XPATH, "//img[contains(@src,'/img/avatar')]")
    UNIQUE_LOCATOR = (By.XPATH, "//*[contains(text() , 'Dynamic Content')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Iframe"

        self.unique_element = WebElement(self.browser, self.UNIQUE_LOCATOR,
                                         description="Dynamic content  page -> img`s")

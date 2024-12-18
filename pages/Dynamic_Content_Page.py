from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.web_element import WebElement


class DynamicContentPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(@class , 'example')]")

    IMG = (By.XPATH, "//img[contains(@src,'/img/avatar')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Iframe"

        self.take_img = WebElement(self.browser, self.IMG,
                                   description="Dynamic content  page -> img`s")

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.class_web_element import WebElement


class DynamicContent(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(@class , 'example')]")

    IMG = (By.XPATH, "//img[contains(@src,'/img/avatar')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Iframe"

        self.take_img = WebElement(self.browser, self.IMG,
                                   description="Dynamic content  page -> img`s")

    def get_image_sources(self):
        images = self.take_img.wait_for_presence()
        return [img.get_attribute("src") for img in images]

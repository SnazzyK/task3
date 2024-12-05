from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class DynamicContent(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[@class = 'example']")

    IMG = (By.XPATH, "//img[contains(@src,'/img/avatar')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Iframe"

        self.take_img = WebElement(self.driver, self.IMG,
                                   description="Dynamic content  page ->  img`s")

    def get_image_sources(self):
        images = self.take_img.wait_for_all_visible()
        return [img.get_attribute("src") for img in images]

    def has_matching_images(self, image_sources):
        return len(set(image_sources)) < len(image_sources)

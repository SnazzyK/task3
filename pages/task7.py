from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class Handlers(BasePage):
    UNIQUE_LOC = (By.XPATH, "//h3[contains(text(),'Opening a new window')]")

    BUTTON_CLICK = (By.XPATH, "//*[contains(text(),'Click Here')]")
    TEXT_PAGE = (By.XPATH, "//h3[contains(text(),'New Window')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'Handlers'
        self.unique_element = Label(self.driver, self.UNIQUE_LOC)

        self.button_click = Button(self.driver, self.BUTTON_CLICK,
                                   description="Handlers page ->  click button")
        self.text_page = Label(self.driver, self.TEXT_PAGE,
                               description="Handlers page ->  text page")

    def click_button(self):
        self.button_click.click()

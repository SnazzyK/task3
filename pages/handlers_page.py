from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.button import Button
from base.label import Label


class HandlersPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//h3[contains(text(),'Opening a new window')]")

    BUTTON_CLICK = (By.XPATH, "//*[contains(text(),'Click Here')]")
    TEXT_PAGE = (By.XPATH, "//h3[contains(text(),'New Window')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'Handlers'
        self.unique_element = Label(self.browser, self.UNIQUE_LOC)

        self.click_button = Button(self.browser, self.BUTTON_CLICK,
                                   description="Handlers page ->  click button")
        self.text_page = Label(self.browser, self.TEXT_PAGE,
                               description="Handlers page ->  text page")

    def click_button_handler(self):
        self.click_button.click()

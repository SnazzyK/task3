from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.label import Label
from base.web_element import WebElement
from conftest import driver


class IFramePage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//h3[contains(text(),'JavaScript Alerts')]")

    CARD_CLICK = (By.XPATH, "//div[contains(@class , 'card mt-4 top-card')][3]")
    NESTED_FRAMES_CLICK = (By.XPATH, "//span[text() = 'Nested Frames']")
    PARENT_FRAME_TEXT = (By.XPATH, "//body")
    CHILD_IFRAME_TEXT = (By.XPATH, "//body")
    FRAMES_CLICK = (By.XPATH, "//*[@id='item-2']//span[contains(text(),'Frames')]")
    FRAMES_TEXT_1 = (By.ID, "sampleHeading")
    NESTED_IFRAME_1 = (By.ID, "frame1")
    NESTED_IFRAME_2 = (By.XPATH, "//iframe[@srcdoc]")
    IFRAME_1 = (By.ID, "frame1")
    IFRAME_2 = (By.ID, "frame1")
    IFRAME_TEXT = (By.ID, "sampleHeading")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Iframe"

        self.unique_element = WebElement(self.browser, self.UNIQUE_LOC, description="unique element")

        self.click_card = Label(self.browser, self.CARD_CLICK,
                                description="demoqa main  page ->  click card")
        self.click_nested_frames = Label(self.browser, self.NESTED_FRAMES_CLICK,
                                         description="alerts Windows page ->  click nested frames")
        self.text_child = Label(self.browser, self.CHILD_IFRAME_TEXT,
                                description="nested frames page ->  text nested frames")
        self.text_parent = Label(self.browser, self.PARENT_FRAME_TEXT,
                                 description="nested frames page ->  text nested frames")
        self.click_frame = Label(self.browser, self.FRAMES_CLICK,
                                 description="frame card page ->  click frame")
        self.text1_frame = Label(self.browser, self.FRAMES_TEXT_1,
                                 description="frame card page -> text frame")

        self.nested_iframe_1 = Label(self.browser, self.NESTED_IFRAME_1,
                                     description="frame card page -> move Iframe_1")
        self.nested_iframe_2 = Label(self.browser, self.NESTED_IFRAME_2,
                                     description="frame card page -> move Iframe_2")
        self.iframe_1 = Label(self.browser, self.IFRAME_1,
                              description="frame card page -> move Iframe_1")
        self.iframe_2 = Label(self.browser, self.IFRAME_2,
                              description="frame card page -> move Iframe_2")
        self.text_iframe = Label(self.browser, self.IFRAME_TEXT,
                                 description="frame card page -> text Iframe")

    def click_main_card(self):
        self.click_card.click()

    def click_nested_frames_card(self):
        self.click_nested_frames.click()

    def wait_nested_iframe_1(self):
        self.nested_iframe_1.wait_for_visible()

    def wait_nested_iframe_2(self):
        self.nested_iframe_2.wait_for_visible()

    def wait_iframe_1(self):
        self.iframe_1.wait_for_visible()

    def wait_iframe_2(self):
        self.iframe_2.wait_for_visible()

    def click_frames(self):
        self.click_frame.click()

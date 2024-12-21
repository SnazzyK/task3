import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from base.button import Button
from base.input import Input
from base.label import Label
from base.web_element import WebElement
from conftest import driver


class FileUploadPage(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[contains(@class , 'example')]")

    BUTTON_CHOOSE = (By.ID, "file-upload")
    BUTTON_UPLOAD = (By.ID, "file-submit")
    TEXT_UPLOAD = (By.XPATH, "//*[@id = 'content']//h3")
    TEXT_FILE = (By.ID, "uploaded-files")
    DRAG_DROP = (By.ID, "drag-drop-upload")
    TEXT_DRAG_DROP = (By.XPATH, "//*[@id = 'drag-drop-upload']//*[@data-dz-name='']")
    ELEM_DRAG_DROP = (By.XPATH, "//*[@id = 'drag-drop-upload']//*[@class='dz-success-mark']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "File"

        self.unique_element = WebElement(self.browser, self.UNIQUE_LOC, description="unique element")

        self.button_choose_file = Input(self.browser, self.BUTTON_CHOOSE,
                                        description="file  page -> added file")

        self.button_drag_drop = Input(self.browser, self.DRAG_DROP,
                                      description="file  page -> added file")

        self.button_upload = Button(self.browser, self.BUTTON_UPLOAD,
                                    description="file page -> click button upload file")

        self.text_upload = Label(self.browser, self.TEXT_UPLOAD,
                                 description="upload page -> get upload text")

        self.text_file = Label(self.browser, self.TEXT_FILE,
                               description="upload page -> get file text")

        self.text_drag_drop = Label(self.browser, self.TEXT_DRAG_DROP,
                                    description="file page -> get file text")

        self.elem_drag_drop = Label(self.browser, self.ELEM_DRAG_DROP,
                                    description="file page -> get file elem")

        self.actions = ActionChains(self.browser.driver)

    def send_file(self, value):
        self.button_choose_file.send_keys(value)
        self.button_upload.click()

    def wait_drop_windows(self):
        return self.button_drag_drop.wait_for_visible()

    def wait_text_drag_drop(self):
        self.text_drag_drop.wait_for_visible()
        self.elem_drag_drop.wait_for_visible()

    def click_button_and_move_file(self, element, file_path):
        self.button_drag_drop.move_and_context_click(element)
        time.sleep(1)
        pyautogui.write(file_path)
        pyautogui.press('enter')
        self.wait_text_drag_drop()

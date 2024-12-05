from selenium.webdriver.common.by import By

from base.base_element import BaseElement, Button, Input, WebElement, Label
from base.base_page import BasePage


class FileUpload(BasePage):
    UNIQUE_LOC = (By.XPATH, "//*[@class = 'example']")

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

        self.button_choose_file = Input(self.driver, self.BUTTON_CHOOSE,
                                        description="file  page ->  added file")

        self.button_drag_drop = Input(self.driver, self.DRAG_DROP,
                                      description="file  page ->  added file")

        self.button_upload = Button(self.driver, self.BUTTON_UPLOAD,
                                    description="file  page ->  upload file")

        self.text_upload = Label(self.driver, self.TEXT_UPLOAD,
                                 description="upload page -> upload text")

        self.text_file = Label(self.driver, self.TEXT_FILE,
                               description="upload page -> file text")

        self.text_drag_drop = Label(self.driver, self.TEXT_DRAG_DROP,
                                    description="file page -> file text")

        self.elem_drag_drop = Label(self.driver, self.ELEM_DRAG_DROP,
                                    description="file page -> file elem")

    def send_file(self, value):
        self.button_choose_file.send_keys(value)
        self.button_upload.click()

    def drag_drop_windows(self):
        return self.button_drag_drop.wait_for_visible()

    def find_text_drag_drop(self):
        self.text_drag_drop.wait_for_visible()
        self.elem_drag_drop.wait_for_visible()

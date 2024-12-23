from config.data_reader import DataReader

from utilities.browser import Browser


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None
        json_config = DataReader(DataReader.FILE_CONFIG)

    def wait_for_open(self):
        return self.unique_element.wait_for_visible()


from selenium.webdriver.support.wait import WebDriverWait

from config.data_reader import DataReader

from utilities.browser import Browser


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    json_config = DataReader(DataReader.FILE_CONFIG)

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

    def wait_for_open(self):
        self.unique_element.wait_for_presence()

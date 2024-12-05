from selenium.webdriver.support.wait import WebDriverWait

from config.data_reader import DataReader
from utilities.browser import Browser, json_config


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    json_config = DataReader(DataReader.FILE_CONFIG)

    def __init__(self, driver):
        self.driver = driver
        self.page_name = None
        self.unique_element = None

        self.wait = WebDriverWait(Browser.get(), json_config.get_data_key("TIMEOUT"))

    def wait_for_open(self):
        self.unique_element.wait_for_presence()

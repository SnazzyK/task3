from selenium.webdriver.support.wait import WebDriverWait

from base.base_element import BaseElement
from utilities.logg_settings import Logger
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)


class Input(BaseElement):

    def send_keys(self, value):
        Logger.logger.info(f"send keys: {self.description}, SEND TEXT: {value}")
        self.wait_for_visible().send_keys(value)

    def clear(self):
        Logger.logger.info(f"clear field:{self.description}")
        self.wait_for_visible().clear()

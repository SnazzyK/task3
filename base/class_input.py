from selenium.webdriver.support.wait import WebDriverWait

from base.base_element import BaseElement
from utilities.logg_settings import Logg
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)


class Input(BaseElement):

    def send_keys(self, value):
        Logg.logger.info(f"send keys: {self.description}, SEND TEXT: {value}")
        WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.visibility_of_element_located(self.locator_name)
        ).send_keys(value)

    def clear(self):
        Logg.logger.info(f"clear field:{self.description}")
        WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.visibility_of_element_located(self.locator_name)).clear()

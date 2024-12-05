from utilities.logg_settings import Logg
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from config.data_reader import DataReader
from conftest import driver

json_config = DataReader(DataReader.FILE_CONFIG)


class BaseElement(BasePage):

    def __init__(self, driver, locator_name=None, description=None):
        super().__init__(driver)
        self.driver = driver
        self.locator_name = locator_name
        self.description = description

    def click(self):
        self.wait.until(
            EC.element_to_be_clickable(self.locator_name)).click()
        Logg.logger.info("click element")

    def wait_for_presence(self):
        Logg.logger.info("Wait presents element")
        return self.wait.until(
            EC.presence_of_element_located(self.locator_name))

    def wait_for_all_presence(self):
        Logg.logger.info("Wait presents all element")
        return self.wait.until(
            EC.presence_of_all_elements_located(self.locator_name))

    def wait_for_visible(self):
        Logg.logger.info("Wait visible element")
        return self.wait.until(
            EC.visibility_of_element_located(self.locator_name))

    def wait_for_all_visible(self):
        Logg.logger.info("Wait visible all element")
        return self.wait.until(
            EC.visibility_of_all_elements_located(self.locator_name))

    def get_text(self):
        Logg.logger.info("get text")
        elem = self.wait.until(
            EC.visibility_of_element_located(self.locator_name))
        return elem.text


class Input(BaseElement):

    def send_keys(self, value):
        self.wait.until(
            EC.visibility_of_element_located(self.locator_name)).send_keys(value)
        Logg.logger.info("send keys")

    def send_keys_for_alert(self, value):
        self.wait.until(EC.alert_is_present()).send_keys(value)
        Logg.logger.info("send keys for alert")

    def clear(self):
        self.wait.until(
            EC.visibility_of_element_located(self.locator_name)).clear()
        Logg.logger.info("clear field")


class Button(BaseElement):
    pass


class Label(BaseElement):
    pass


class WebElement(BaseElement):
    pass

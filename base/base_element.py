from selenium.webdriver.support.wait import WebDriverWait

from utilities.logg_settings import Logg
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)


class BaseElement:
    def __init__(self, browser, locator_name=None, description=None):
        self.browser = browser
        self.locator_name = locator_name
        self.description = description

    def click(self):
        Logg.logger.info("Click element")
        WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.element_to_be_clickable(self.locator_name)
        ).click()

    def wait_for_presence(self):
        Logg.logger.info("Wait presents element")
        return WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.presence_of_element_located(self.locator_name))


    def wait_for_all_presence(self):
        Logg.logger.info("Wait presents all element")
        WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.presence_of_all_elements_located(self.locator_name))

    def wait_for_visible(self):
        Logg.logger.info("Wait visible element")
        element = WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.visibility_of_element_located(self.locator_name))
        return element

    def wait_for_all_visible(self):
        Logg.logger.info("Wait visible all element")
        return WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.visibility_of_all_elements_located(self.locator_name))

    def get_text(self):
        Logg.logger.info(f"get text")
        elem = WebDriverWait(self.browser.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.visibility_of_element_located(self.locator_name))
        text = elem.text
        Logg.logger.info(f"Extracted text: {text}")
        return text



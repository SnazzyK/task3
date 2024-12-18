from bs4 import BeautifulSoup
from scripts.regsetup import description
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logg_settings import Logger
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)


class BaseElement:
    def __init__(self, browser, locator, description=None):
        self.browser = browser
        self.locator = locator
        self.description = description
        self.timeout = 10

    def click(self):
        Logger.logger.info(f"Attempting to click element: {self.description}")
        WebDriverWait(self.browser.driver, self.timeout).until(
            EC.element_to_be_clickable(self.locator)
        ).click()

    def wait_for_presence(self):
        Logger.logger.info(f"Waiting for presents element : {self.description}")
        return WebDriverWait(self.browser.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator))

    def wait_for_visible(self):
        Logger.logger.info(f"Waiting for visibility of element: {self.description}")
        element = WebDriverWait(self.browser.driver, self.timeout).until(
            EC.visibility_of_element_located(self.locator))
        return element

    def get_text(self):
        Logger.logger.info(f"Getting text from element: {self.description}")
        elem = self.wait_for_visible()
        text = elem.text
        Logger.logger.info(f"Extracted text from '{self.description}': {text}")
        return text

    def execute_script_scroll_to(self):
        Logger.logger.info(f"Window scroll to : {self.description}")
        self.browser.execute_script_wrapper("window.scrollTo(0, document.body.scrollHeight);")

    def move_and_context_click(self, element):
        Logger.logger.info(f"move to element and context click : {self.description}")
        action = ActionChains(self.browser.driver)
        action.move_to_element(element).context_click().perform()

    def switch_to_frame(self):
        Logger.logger.info(f"Switch to iframe : {self.description}")
        element = WebDriverWait(self.browser.driver, self.timeout).until(
            EC.visibility_of_element_located(self.locator))
        return self.browser.switch_iframe_wrapper(element)

    def get_attribute_wrapper(self, value):
        return self.browser.driver.get_attribute(value)

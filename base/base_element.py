from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logg_settings import Logger
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)


class BaseElement:
    TIMEOUT = 10

    def __init__(self, browser, locator, description=None):
        self.browser = browser
        self.locator = locator
        self.description = description

    def click(self):
        Logger.logger.info(f"Click element: {self.description}")
        WebDriverWait(self.browser.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(self.locator)
        ).click()

    def wait_for_presence(self):
        Logger.logger.info(f"Wait for presents element : {self.description}")
        return WebDriverWait(self.browser.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(self.locator))

    def wait_for_visible(self):
        Logger.logger.info(f"Wait for visibility of element: {self.description}")
        element = WebDriverWait(self.browser.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.locator))
        return element

    def get_text(self):
        Logger.logger.info(f"Get text from element: {self.description}")
        elem = self.wait_for_presence()
        text = elem.text
        Logger.logger.info(f"Extracted text from '{self.description}': {text}")
        return text

    def switch_to_frame(self):
        Logger.logger.info(f"Switch to iframe : {self.description}")
        element = self.wait_for_presence()
        return self.browser.switch_iframe_wrapper(element)

    def move_and_context_click(self, element):
        Logger.logger.info(f"Move to element and context click")
        action = ActionChains(self.browser.driver)
        action.move_to_element(element).click().perform()

    def click_js(self):
        Logger.logger.info("Click and wait button prompt js")
        self.browser.driver.execute_script("arguments[0].click()", self.locator.wait_for_presence())

    def get_inner_html(self):
        Logger.logger.info(f"Gett inner HTML for element: {self.locator}")
        element = self.wait_for_presence()
        return element.get_attribute("innerHTML")

    def get_elements(self, tag, class_el):
        Logger.logger.info(f"Parsing HTML for elements with tag: {tag}, class: {class_el}")
        inner_html = self.get_inner_html()
        soup = BeautifulSoup(inner_html, "html.parser")
        return soup.find_all(tag, class_=class_el)

    def get_element(self, tag, types, value):
        Logger.logger.info(f"Get element with tag: {tag}, type-value: {types}:{value}")
        inner_html = self.get_inner_html()
        soup = BeautifulSoup(inner_html, "html.parser")
        element = soup.find(tag, {types: value})
        return element

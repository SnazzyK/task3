import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader

from utilities.logg_settings import Logger

json_config = DataReader(DataReader.FILE_CONFIG)


class Browser:
    def __init__(self, driver):
        Logger.logger.info("init new browser")
        self.driver = driver
        self.timeout = 10

    def get(self, url):
        Logger.logger.info(f"go to url: {url}")
        self.driver.get(url)

    def close(self):
        Logger.logger.info("Close window browser")
        self.driver.close()

    def quit(self):
        Logger.logger.info("Quit browser")
        self.driver.quit()

    def refresh(self):
        Logger.logger.info("Refresh browser")
        self.driver.refresh()

    def execute_script_wrapper(self, script, *args):
        Logger.logger.info(f"Executing JavaScript: {script} with arguments: {args}")
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            Logger.logger.error(f"Error executing JavaScript: {script}, error: {e}")
            raise

    def accept_alert(self):
        Logger.logger.info("Alert accept")
        WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()).accept()

    def dismiss_alert(self):
        Logger.logger.info("Dismiss alert")
        WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()).dismiss()

    def get_text_alert(self):
        Logger.logger.info("Get text alert")
        return WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()).text

    def send_keys_alert(self, text):
        Logger.logger.info(f"Send text in alert: {text}")
        WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()).send_keys(text)

    def switch_handler(self, value):
        Logger.logger.info(f"Switch to handler: {value}")
        self.driver.switch_to.window(self.driver.window_handles[value])

    def get_title_handler(self):
        Logger.logger.info("Get name handler")
        return self.driver.title

    def switch_iframe_wrapper(self, iframe):
        Logger.logger.info("Switch iframe-wrapper")
        self.driver.switch_to.frame(iframe)

    def switch_default(self):
        Logger.logger.info("Switch to main content")
        return self.driver.switch_to.default_content()

    def get_elements(self, tag, class_el):
        Logger.logger.info("Get elements ")
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        elements = soup.find_all(tag, class_=class_el)
        return elements

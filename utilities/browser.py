import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.data_reader import DataReader
from utilities.logg_settings import Logg

json_config = DataReader(DataReader.FILE_CONFIG)


class Browser:
    def __init__(self):
        Logg.logger.info("Инициализация нового драйвера")
        chrome_options = Options()
        chrome_options.add_argument(json_config.get_data("Chrome_options", 0))
        self.driver = webdriver.Chrome(options=chrome_options)

    def get(self, url):
        Logg.logger.info(f"Переход по URL: {url}")
        self.driver.get(url)

    def close(self):
        Logg.logger.info("Close window browser")
        self.driver.close()

    def quit(self):
        Logg.logger.info("Quit browser")
        self.driver.quit()

    def refresh(self):
        Logg.logger.info("Refresh browser")
        self.driver.refresh()

    def scroll(self, x, y):
        Logg.logger.info(f"Scroll browser ({x},{y})")
        self.driver.execute_script(f"window.scrollTo({x},{y});")

    def wait_alert(self):
        Logg.logger.info("Wait alert")
        return WebDriverWait(self.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.alert_is_present()
        )

    def accept_alert(self):
        Logg.logger.info("Alert accept")
        self.wait_alert().accept()

    def dismiss_alert(self):
        Logg.logger.info("Dismiss alert")
        self.wait_alert().dismiss()

    def get_text_alert(self):
        Logg.logger.info("Get text alert")
        return self.wait_alert().text

    def send_keys_alert(self, text):
        Logg.logger.info(f"Send text in alert: {text}")
        self.wait_alert().send_keys(text)

    def switch_handler(self, value):
        Logg.logger.info(f"Switch to handler: {value}")
        self.driver.switch_to.window(self.driver.window_handles[value])

    def get_title_handler(self):
        Logg.logger.info("Get name handler")
        return self.driver.title

    def switch_iframe(self, iframe_identifier):
        Logg.logger.info(f"Switch to iframe: {iframe_identifier}")
        return self.driver.switch_to.frame(iframe_identifier)

    def switch_default(self):
        Logg.logger.info("Switch to main content")
        return self.driver.switch_to.default_content()



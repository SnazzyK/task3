from selenium.common import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.data_reader import DataReader
from utilities.logg_settings import Logger

json_config = DataReader(DataReader.FILE_CONFIG)


class Browser:
    TIMEOUT = 10

    def __init__(self, driver):
        Logger.logger.info("init new browser")
        self.driver = driver

    def get(self, url):
        Logger.logger.info(f"Go to url: {url}")
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

    def execute_script_scroll_to(self):
        Logger.logger.info(f"Window scroll ")
        self.driver.execute_script_wrapper("window.scrollTo(0, document.body.scrollHeight);")

    def execute_script(self, script, *args):
        Logger.logger.info(f"Execute JavaScript: {script} with arguments: {args}")
        try:
            return self.driver.execute_script(script, *args)
        except WebDriverException as e:
            Logger.logger.error(f"Error executing JavaScript: {script}, error: {e}")
            raise

    def accept_alert(self):
        Logger.logger.info("Alert accept")
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.alert_is_present()).accept()

    def dismiss_alert(self):
        Logger.logger.info("Dismiss alert")
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.alert_is_present()).dismiss()

    def get_text_alert(self):
        Logger.logger.info("Get text alert")
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.alert_is_present()).text

    def send_keys_alert(self, text):
        Logger.logger.info(f"Send text in alert: {text}")
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.alert_is_present()).send_keys(text)

    def switch_handler(self, value):
        Logger.logger.info(f"Switch to handler: {value}")
        self.driver.switch_to.window(self.driver.window_handles[value])

    def get_title_handler(self):
        Logger.logger.info("Get name handler")
        return self.driver.title

    def switch_iframe_wrapper(self, iframe):
        Logger.logger.info("Switch iframe-wrapper")
        return self.driver.switch_to.frame(iframe)

    def switch_default(self):
        Logger.logger.info("Switch to main content")
        self.driver.switch_to.default_content()

    def switch_to_frame(self, element):
        Logger.logger.info(f"Switch to iframe ")
        return self.switch_iframe_wrapper(element)

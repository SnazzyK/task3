import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)

class Browser:
    def __init__(self):
        logging.info("Initializing new driver instance")
        chrome_options = Options()
        chrome_options.add_argument(json_config.get_data("Chrome_options", 0))
        self.driver = webdriver.Chrome(options=chrome_options)

    def get(self):
        logging.info("Navigating to URL")
        return self.driver

    def close(self):
        logging.info("Closing the browser window")
        self.driver.close()

    def quit(self):
        logging.info("Quitting the browser session")
        self.driver.quit()

    def refresh(self):
        logging.info("Refreshing the browser")
        self.driver.refresh()

    def scroll(self, x, y):
        logging.info("Scrolling in the browser")
        self.driver.execute_script(f"window.scrollTo({x},{y});")


    def get_alert(self):
        logging.info("get alert")
        return WebDriverWait(self.driver, json_config.get_data_key("TIMEOUT")).until(
            EC.alert_is_present()
        )


    def accept_to_alert(self):
        logging.info("accept alert")
        self.get_alert().accept()


    def dismiss_to_alert(self):
        logging.info("dismiss alert")
        self.get_alert().dismiss()


    def get_text_to_alert(self):
        logging.info("get text alert")
        return self.get_alert().text


    def send_keys_alert(self, text):
        logging.info("send keys alert")
        self.get_alert().send_keys(text)


    def switch_handler(self, value):
        logging.info("switch handler")
        self.driver.switch_to.window(self.driver.window_handles[value])


    def get_title_handler(self):
        logging.info("get title handler")
        return self.driver.title


    def switch_iframe(self, iframe_identifier):
        logging.info("switch iframe")
        self.driver.switch_to.frame(iframe_identifier)


    def switch_default(self):
        logging.info("switch handler default")
        return self.driver.switch_to.default_content()



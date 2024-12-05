import logging

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from config.data_reader import DataReader

json_config = DataReader(DataReader.FILE_CONFIG)


class Browser:
    driver = None

    @classmethod
    def initialize_driver(cls):
        if cls.driver is None:
            chrome_options = Options()
            chrome_options.add_argument(json_config.get_data("Chrome_options", 0))
            cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def get(cls):
        if cls.driver is None:
            cls.initialize_driver()
        return cls.driver

    @classmethod
    def close(cls):
        cls.driver.close()
        logging.info("handle close")

    @classmethod
    def quit(cls):
        cls.driver.quit()
        logging.info("handle quit")

    @classmethod
    def refresh(cls):
        return cls.driver.refresh()

    @classmethod
    def accept_to_alert(cls):
        cls.driver.switch_to.alert.accept()

    @classmethod
    def dismiss_to_alert(cls):
        cls.driver.switch_to.alert.dismiss()

    @classmethod
    def get_text_to_alert(cls):
        alert = cls.driver.switch_to.alert
        alert_text = alert.text
        return alert_text

    @classmethod
    def send_keys_alert(cls, text):
        cls.driver.switch_to.alert.send_keys(text)

    @classmethod
    def switch_handler(cls, value):
        cls.driver.switch_to.window(cls.driver.window_handles[value])

    @classmethod
    def get_title_handler(cls):
        return cls.driver.title

    @classmethod
    def switch_iframe(cls, iframe_identifier):
        cls.driver.switch_to.frame(iframe_identifier)

    @classmethod
    def switch_default(cls):
        return cls.driver.switch_to.default_content()

    @classmethod
    def scroll(cls, x, y):
        cls.driver.execute_script(f"window.scrollTo({x},{y});")

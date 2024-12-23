import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.data_reader import DataReader
from utilities.browser_type import BrowserType

from utilities.logg_settings import Logger

json_config = DataReader(DataReader.FILE_CONFIG)


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name=BrowserType.CHROME.value):
        Logger.logger.info(f"Creating a browser instance: {browser_name}")
        browser_name = browser_name.lower()

        if browser_name == BrowserType.CHROME.value:
            chrome_options = Options()
            chrome_options.add_argument(json_config.get_data("Chrome_options", 0))
            driver = webdriver.Chrome(options=chrome_options)

        elif browser_name == BrowserType.FIREFOX.value:
            firefox_options = Options()
            firefox_options.add_argument(json_config.get_data("Firefox_options", 0))
            driver = webdriver.Firefox(options=firefox_options)

        elif browser_name == BrowserType.EDGE.value:
            edge_options = Options()
            edge_options.add_argument(json_config.get_data("Edge_options", 0))
            driver = webdriver.Edge(options=edge_options)

        else:
            raise ValueError(f"Неизвестный браузер: {browser_name}")

        return driver

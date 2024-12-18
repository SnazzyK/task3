import pytest

from config.data_reader import DataReader
from utilities.Browser_Factory import BrowserFactory
from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)

import logging


@pytest.fixture(scope="function", autouse=False)
def driver():
    logging.info("Launching the browser")
    driver_instance = BrowserFactory.get_browser("chrome")
    browser = Browser(driver_instance)
    yield browser
    logging.info("Закрытие браузера")
    browser.quit()


@pytest.fixture(scope="session")
def config_reader():
    return DataReader(DataReader.FILE_CONFIG)

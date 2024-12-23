import pytest

from config.data_reader import DataReader
from utilities.browser_factory import BrowserFactory
from utilities.browser import Browser
from utilities.browser_type import BrowserType

json_config = DataReader(DataReader.FILE_CONFIG)

import logging


@pytest.fixture(scope="function", autouse=False)
def driver():
    driver_instance = BrowserFactory.get_browser(BrowserType.CHROME)
    browser = Browser(driver_instance)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def config_reader():
    return DataReader(DataReader.FILE_CONFIG)

import pytest

from config.data_reader import DataReader
from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)

import logging


@pytest.fixture(scope="function", autouse=False)
def driver():
    logging.debug("Запуск браузера")
    browser1 = Browser()
    yield browser1
    logging.info("Закрытие браузера")
    browser1.quit()

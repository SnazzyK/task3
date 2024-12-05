import pytest

from config.data_reader import DataReader
from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)

import logging


@pytest.fixture(scope="function", autouse=False)
def driver():
    logging.info("Запуск браузера")
    driver = Browser.get()

    yield driver
    logging.info("Закрытие браузера")
    Browser.quit()

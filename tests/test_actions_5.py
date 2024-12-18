import random
import time
from itertools import count

import pytest
from selenium.webdriver import ActionChains

from config.data_reader import DataReader
from conftest import config_reader

from pages.Actions_Page import ActionsPage


@pytest.mark.parametrize("value1, value2, expected_result", [
    (1, 10, "Horizontal Slider"),
])
def test_slider(driver, value1, value2, expected_result, config_reader):
    driver.get(config_reader.get_data_key("URL-4"))
    action = ActionsPage(driver)
    text_unique = action.get_unique_element_text()
    assert text_unique == expected_result, f"Actual result:{text_unique}\nExpected result:{expected_result}"
    score = random.randint(value1, value2)
    value = action.random_move_slider(score)
    text = action.get_result_slider()
    value2 = action.get_format_number(value)
    assert text == f"{value2}", f"Actual result:{text}\nExpected result:{value2}"

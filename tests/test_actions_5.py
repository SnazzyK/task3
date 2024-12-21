import random
import time
from itertools import count

import pytest
from selenium.webdriver import ActionChains

from config.data_reader import DataReader
from conftest import config_reader

from pages.actions_page import ActionsPage


@pytest.mark.parametrize("value1, value2, expected_result", [
    (1, 10, "Horizontal Slider"),
])
def test_slider(driver, value1, value2, expected_result, config_reader):
    driver.get(config_reader.get_data_key("URL-4"))
    action = ActionsPage(driver)
    action.wait_for_open()
    step = driver.get_element("input", "type", "range").get("step", None)
    score = random.randint(value1, value2)
    value = action.random_move_slider(score, step)
    text = action.get_result_slider()
    value2 = action.get_format_number(value)
    assert text == f"{value2}", f"Actual result:{text}\nExpected result:{value2}"

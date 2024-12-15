import random
import time
from itertools import count

from selenium.webdriver import ActionChains

from config.data_reader import DataReader

from pages.task5 import Actions

json_config = DataReader(DataReader.FILE_CONFIG)
VALUE1 = 1
VALUE2 = 10
count = random.randint(VALUE1,VALUE2)




def test_slider(driver):
    driver.get(json_config.get_data_key("URL-4"))
    action = Actions(driver)
    text_unique = action.unique_element_text()
    assert text_unique == f"Horizontal Slider", f"Actual result:{text_unique}\nExpected result:Horizontal Slider"
    value = action.random_move_slider(count)
    time.sleep(1)
    text = action.slider_result()
    value2 =action.format_number(value)
    assert text == f"{value2}", f"Actual result:{text}\nExpected result:{value2},random count = {count}"






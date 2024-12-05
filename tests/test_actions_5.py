import random

from config.data_reader import DataReader

from pages.task5 import Actions

json_config = DataReader(DataReader.FILE_CONFIG)

random_number = random.choice(range(-40, 51, 10))

value_mapping = {
    -40: 0.5,
    -30: 1,
    -20: 1.5,
    -10: 2,
    0: 2.5,
    10: 3,
    20: 3.5,
    30: 4,
    40: 4.5,
    50: 5
}

random_result = value_mapping.get(random_number)


def test_slider(driver):
    driver.get(json_config.get_data_key("URL-4"))
    action = Actions(driver)
    action.move_slider(random_number)
    text = action.slider_result.get_text()
    assert text == f"{random_result}", f"Actual result:{text}\nExpected result:{random_number}"

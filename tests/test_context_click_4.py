from config.data_reader import DataReader

from pages.task4 import AlertsContextClick
from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)


def test_box_for_js(driver):
    driver.get(json_config.get_data_key("URL-3"))
    acc = AlertsContextClick(driver)
    acc.click_box()
    text_alert = driver.get_text_to_alert()
    assert text_alert == "You selected a context menu"
    driver.accept_to_alert()

from config.data_reader import DataReader

from pages.task2 import JsAlert
from utilities.browser import Browser
from faker import Faker

json_config = DataReader(DataReader.FILE_CONFIG)
fake = Faker()
random_value = str(fake.random_int(min=1, max=10))


def test_alerts(driver):
    driver.get(json_config.get_data_key("URL-2"))
    js = JsAlert(driver)

    js.click_button_alert()
    text_alert = Browser.get_text_to_alert()
    assert text_alert == "I am a JS Alert"
    Browser.accept_to_alert()
    text_result_alert = js.result.get_text()
    assert text_result_alert == "You successfully clicked an alert", f"Actual result:{text_result_alert}\nExpected result:You successfully clicked an alert"

    js.click_button_confirm()
    text_confirm = Browser.get_text_to_alert()
    assert text_confirm == "I am a JS Confirm"
    Browser.accept_to_alert()
    text_result_confirm = js.result.get_text()
    assert text_result_confirm == "You clicked: Ok", f"Actual result:{text_result_confirm}\nExpected result:You clicked: Ok"

    js.click_button_prompt()
    text_prompt = Browser.get_text_to_alert()
    assert text_prompt == "I am a JS prompt"
    value = Browser.send_keys_alert(random_value)
    Browser.accept_to_alert()
    text_result_prompt = js.result.get_text()
    assert text_result_prompt == f"You entered: {random_value}", f"Actual result: {text_result_prompt}\nExpected result:You entered: {random_value}"


def test_alerts_for_js(driver):
    driver.get(json_config.get_data_key("URL-2"))
    js = JsAlert(driver)

    js.click_button_alert_js()
    text_alert = Browser.get_text_to_alert()
    assert text_alert == "I am a JS Alert"
    Browser.accept_to_alert()
    text_result_alert = js.result.get_text()
    assert text_result_alert == "You successfully clicked an alert", f"Actual result:{text_result_alert}\nExpected result:You successfully clicked an alert"

    js.click_button_confirm_js()
    text_confirm = Browser.get_text_to_alert()
    assert text_confirm == "I am a JS Confirm"
    Browser.accept_to_alert()
    text_result_confirm = js.result.get_text()
    assert text_result_confirm == "You clicked: Ok", f"Actual result:{text_result_confirm}\nExpected result:You clicked: Ok"

    js.click_button_prompt_js()
    text_prompt = Browser.get_text_to_alert()
    assert text_prompt == "I am a JS prompt"
    value = Browser.send_keys_alert(random_value)
    Browser.accept_to_alert()
    text_result_prompt = js.result.get_text()
    assert text_result_prompt == f"You entered: {random_value}", f"Actual result: {text_result_prompt}\nExpected result:You entered: {random_value}"

import time

from config.data_reader import DataReader

from pages.task2 import JsPage

from faker import Faker

json_config = DataReader(DataReader.FILE_CONFIG)
fake = Faker()
random_value = str(fake.random_int(min=1, max=10))


def test_alerts(driver):
    driver.get(json_config.get_data_key("URL-2"))
    js_page = JsPage(driver)
    js_page.click_button_alert()
    text_alert = driver.get_text_alert()
    assert text_alert == "I am a JS Alert", f"Actual result:{text_alert}\nExpected result:I am a JS Alert"
    driver.accept_alert()
    text_result_alert = js_page.result.get_text()
    assert text_result_alert == "You successfully clicked an alert", f"Actual result:{text_result_alert}\nExpected result:You successfully clicked an alert"

    js_page.click_button_confirm()
    text_confirm = driver.get_text_alert()
    assert text_confirm == "I am a JS Confirm", f"Actual result:{text_confirm}\nExpected result:I am a JS Confirm"
    driver.accept_alert()
    text_result_confirm = js_page.result.get_text()
    assert text_result_confirm == "You clicked: Ok", f"Actual result:{text_result_confirm}\nExpected result:You clicked: Ok"

    js_page.click_button_prompt()
    text_prompt = driver.get_text_alert()
    assert text_prompt == "I am a JS prompt", f"Actual result:{text_prompt}\nExpected result:I am a JS prompt"
    value = driver.send_keys_alert(random_value)
    driver.accept_alert()
    text_result_prompt = js_page.result.get_text()
    assert text_result_prompt == f"You entered: {random_value}", f"Actual result: {text_result_prompt}\nExpected result:You entered: {random_value}"


def test_alerts_for_js(driver):
    driver.get(json_config.get_data_key("URL-2"))
    js_page = JsPage(driver)
    js_page.click_button_alert_js()
    text_alert = driver.get_text_alert()
    assert text_alert == "I am a JS Alert", f"Actual result:{text_alert}\nExpected result:I am a JS Alert"
    driver.accept_alert()
    text_result_alert = js_page.result.get_text()
    assert text_result_alert == "You successfully clicked an alert", f"Actual result:{text_result_alert}\nExpected result:You successfully clicked an alert"

    js_page.click_button_confirm_js()
    text_confirm = driver.get_text_alert()
    assert text_confirm == "I am a JS Confirm", f"Actual result:{text_confirm}\nExpected result:I am a JS Confirm"
    driver.accept_alert()
    text_result_confirm = js_page.result.get_text()
    assert text_result_confirm == "You clicked: Ok", f"Actual result:{text_result_confirm}\nExpected result:You clicked: Ok"

    js_page.click_button_prompt_js()
    text_prompt = driver.get_text_alert()
    assert text_prompt == "I am a JS prompt", f"Actual result: {text_prompt}\nExpected result:I am a JS prompt"
    value = driver.send_keys_alert(random_value)
    driver.accept_alert()
    text_result_prompt = js_page.result.get_text()
    assert text_result_prompt == f"You entered: {random_value}", f"Actual result: {text_result_prompt}\nExpected result:You entered: {random_value}"

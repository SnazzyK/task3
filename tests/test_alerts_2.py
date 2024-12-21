from conftest import json_config

from pages.js_page import JsPage

from faker import Faker

fake = Faker()
random_value = str(fake.random_int(min=1, max=10))
EXPECTED_RESULT_ALERTS = "I am a JS Alert"
EXPECTED_RESULT_ALERTS_RESULT = "You successfully clicked an alert"
EXPECTED_RESULT_CONFIRM = "I am a JS Confirm"
EXPECTED_RESULT_CONFIRM_RESULT = "You clicked: Ok"
EXPECTED_RESULT_PROMPT = "I am a JS prompt"


def test_alerts(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-2"))
    js_page = JsPage(driver)
    js_page.wait_for_open()
    js_page.click_button_alert()
    text_alert = driver.get_text_alert()
    assert text_alert == EXPECTED_RESULT_ALERTS, f"Actual result:{text_alert}\nExpected result:{EXPECTED_RESULT_ALERTS}"
    driver.accept_alert()
    text_result_alert = js_page.result.get_text()
    assert text_result_alert == EXPECTED_RESULT_ALERTS_RESULT, f"Actual result:{text_result_alert}\nExpected result:{EXPECTED_RESULT_ALERTS_RESULT}"

    js_page.click_button_confirm()
    text_confirm = driver.get_text_alert()
    assert text_confirm == EXPECTED_RESULT_CONFIRM, f"Actual result:{text_confirm}\nExpected result:{EXPECTED_RESULT_CONFIRM}"
    driver.accept_alert()
    text_result_confirm = js_page.result.get_text()
    assert text_result_confirm == EXPECTED_RESULT_CONFIRM_RESULT, f"Actual result:{text_result_confirm}\nExpected result:{EXPECTED_RESULT_CONFIRM_RESULT}"

    js_page.click_button_prompt()
    text_prompt = driver.get_text_alert()
    assert text_prompt == EXPECTED_RESULT_PROMPT, f"Actual result:{text_prompt}\nExpected result:{EXPECTED_RESULT_PROMPT}"
    value = driver.send_keys_alert(random_value)
    driver.accept_alert()
    text_result_prompt = js_page.result.get_text()
    assert text_result_prompt == f"You entered: {random_value}", f"Actual result: {text_result_prompt}\nExpected result:You entered: {random_value}"


def test_alerts_for_js(driver):
    driver.get(json_config.get_data_key("URL-2"))
    js_page = JsPage(driver)
    js_page.click_button_alert_js()
    text_alert = driver.get_text_alert()
    assert text_alert == EXPECTED_RESULT_ALERTS, f"Actual result:{text_alert}\nExpected result:{EXPECTED_RESULT_ALERTS}"
    driver.accept_alert()
    text_result_alert = js_page.result.get_text()
    assert text_result_alert == EXPECTED_RESULT_ALERTS_RESULT, f"Actual result:{text_result_alert}\nExpected result:{EXPECTED_RESULT_ALERTS_RESULT}"

    js_page.click_button_confirm_js()
    text_confirm = driver.get_text_alert()
    assert text_confirm == EXPECTED_RESULT_CONFIRM, f"Actual result:{text_confirm}\nExpected result:{EXPECTED_RESULT_CONFIRM}"
    driver.accept_alert()
    text_result_confirm = js_page.result.get_text()
    assert text_result_confirm == EXPECTED_RESULT_CONFIRM_RESULT, f"Actual result:{text_result_confirm}\nExpected result:{EXPECTED_RESULT_CONFIRM_RESULT}"

    js_page.click_button_prompt_js()
    text_prompt = driver.get_text_alert()
    assert text_prompt == EXPECTED_RESULT_PROMPT, f"Actual result: {text_prompt}\nExpected result:{EXPECTED_RESULT_PROMPT}"
    value = driver.send_keys_alert(random_value)
    driver.accept_alert()
    text_result_prompt = js_page.result.get_text()
    assert text_result_prompt == f"You entered: {random_value}", f"Actual result: {text_result_prompt}\nExpected result:You entered: {random_value}"

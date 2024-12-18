from pages.Alerts_Context_Click_Page import AlertsContextClickPage

EXPECTED_RESULT = "You selected a context menu"


def test_box_for_js(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-3"))
    acc = AlertsContextClickPage(driver)
    acc.click_box()
    text_alert = driver.get_text_alert()
    assert text_alert == EXPECTED_RESULT, f"Actual result:{text_alert}\nExpected result:{EXPECTED_RESULT}"
    driver.accept_alert()

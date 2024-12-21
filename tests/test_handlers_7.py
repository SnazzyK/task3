from config.data_reader import DataReader
from pages.handlers_page import HandlersPage

EXPECTED_RESULT = 'New Window'


def test_handlers(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-6"))
    handler = HandlersPage(driver)
    handler.wait_for_open()
    handler.click_button_handler()
    driver.switch_handler(1)
    text_page = handler.text_page.get_text()
    assert text_page == EXPECTED_RESULT, f"Actual result:{text_page}\nExpected result:{EXPECTED_RESULT}"
    text_title = driver.get_title_handler()
    assert text_title == EXPECTED_RESULT, f"Actual result:{text_title}\nExpected result:{EXPECTED_RESULT}"
    driver.switch_handler(0)

    handler.click_button_handler()
    driver.switch_handler(2)
    text_page = handler.text_page.get_text()
    assert text_page == EXPECTED_RESULT, f"Actual result:{text_page}\nExpected result:{EXPECTED_RESULT}"
    text_title = driver.get_title_handler()
    assert text_title == EXPECTED_RESULT, f"Actual result:{text_title}\nExpected result:{EXPECTED_RESULT}"
    driver.switch_handler(0)

    driver.switch_handler(1)
    driver.close()
    driver.switch_handler(1)
    driver.close()

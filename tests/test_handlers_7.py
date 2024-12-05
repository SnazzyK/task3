from config.data_reader import DataReader
from pages.task7 import Handlers
from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)


def test_handlers(driver):
    driver.get(json_config.get_data_key("URL-6"))
    handler = Handlers(driver)

    handler.unique_element.wait_for_visible()
    handler.click_button()
    Browser.switch_handler(1)
    text_page = handler.text_page.get_text()
    assert text_page == 'New Window', f"Actual result:{text_page}\nExpected result:New Window"
    text_title = Browser.get_title_handler()
    assert text_title == 'New Window', f"Actual result:{text_title}\nExpected result:New Window"
    Browser.switch_handler(0)

    handler.unique_element.wait_for_visible()
    handler.click_button()
    Browser.switch_handler(2)
    text_page = handler.text_page.get_text()
    assert text_page == 'New Window', f"Actual result:{text_page}\nExpected result:New Window"
    text_title = Browser.get_title_handler()
    assert text_title == 'New Window', f"Actual result:{text_title}\nExpected result:New Window"
    Browser.switch_handler(0)

    handler.unique_element.wait_for_visible()
    Browser.switch_handler(1)
    Browser.close()
    Browser.switch_handler(1)
    Browser.close()
